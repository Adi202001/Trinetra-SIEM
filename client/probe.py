from socket import socket
import unittest
import logging
import logging.handlers
import subprocess
import pickle
import platform
import time
from multiprocessing import Process

def fetch_windows_logs():
    import win32evtlog
    hand = win32evtlog.OpenEventLog(None, 'System')
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
    return events

def fetch_macos_logs():
    try:
        process = subprocess.Popen(['log', 'show', '--last', '10m'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = process.communicate()
        log_messages = out.decode('utf-8').splitlines()
        return log_messages
    except FileNotFoundError:
        print("Error: 'log' command not found.")
        return []

def fetch_linux_logs():
    try:
        process = subprocess.Popen(['journalctl', '--no-pager'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = process.communicate()
        log_messages = out.decode('utf-8').splitlines()
        return log_messages
    except FileNotFoundError:
        print("Error: 'journalctl' command not found. Using syslog alternative.")
        try:
            process = subprocess.Popen(['tail', '-n', '10', '/var/log/syslog'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, _ = process.communicate()
            log_messages = out.decode('utf-8').splitlines()
            return log_messages
        except FileNotFoundError:
            print("Error: 'tail' command not found.")
            return []

def get_host_ip():
    host = input("Enter the host IP: ")
    return host

def send_logs_to_server(host, port):
    logger = logging.getLogger('system_logger')
    logger.setLevel(logging.INFO)
    sh = logging.handlers.SocketHandler(host, port)
    logger.addHandler(sh)

    try:
        while True:
            if platform.system() == 'Windows':
                events = fetch_windows_logs()
            elif platform.system() == 'Darwin':
                events = fetch_macos_logs()
            elif platform.system() == 'Linux':
                events = fetch_linux_logs()

            for event in events:
                logger.info(event)  # Assuming the log format is suitable for logging.info()

            time.sleep(5)  # Adjust the interval as needed

    except KeyboardInterrupt:
        pass

    finally:
        logger.removeHandler(sh)
        sh.close()

def send_pcap_data_to_server(host, port):
    try:
        process = subprocess.Popen(['tcpdump', '-w', '-', '-U', '-n', '-i', 'eth0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            while True:
                data = process.stdout.read(1024)
                if not data:
                    break
                sock.sendall(data)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error occurred while sending pcap data: {e}")

class TestSystemLogs(unittest.TestCase):
    def test_SendLogsToServer(self):
        host = get_host_ip()
        port = 9000
        server_process = Process(target=send_logs_to_server, args=(host, port))
        server_process.start()
        server_process.join()

    def test_SendPcapDataToServer(self):
        host = get_host_ip()
        port = 9003
        pcap_process = Process(target=send_pcap_data_to_server, args=(host, port))
        pcap_process.start()
        pcap_process.join()

if __name__ == "__main__":
    unittest.main()