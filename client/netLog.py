import subprocess
import threading
import time
import platform
import logging
import logging.handlers
import psutil
import re
import csv

def get_host_ip():
    host = input("Enter the host IP: ")
    return host

def setup_logger():
    logger = logging.getLogger('system_logger')
    sh = logging.handlers.SocketHandler(host, port)
    logger.addHandler(sh)
    return logger, sh

def send_system_logs_to_socket(logger, interval=5):
    try:
        while True:
            # Collect system logs based on the operating system
            if platform.system() == 'Windows':
                send_windows_logs(logger)
            elif platform.system() == 'Darwin':  # macOS
                send_macos_logs(logger)
            elif platform.system() == 'Linux':
                send_linux_logs(logger)

            # Collect memory information
            send_memory_info(logger)

            time.sleep(interval)

    except KeyboardInterrupt:
        pass  # Allow the script to be interrupted gracefully

    finally:
        logger.removeHandler(sh)
        sh.close()

def send_windows_logs(logger):
    try:
        import win32evtlog

        hand = win32evtlog.OpenEventLog(None, 'System')
        total = win32evtlog.GetNumberOfEventLogRecords(hand)

        events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
        for event in events:
            log_message = event.StringInserts[0] if event.StringInserts else ''
            print('Windows Log message before sending:', log_message)
            logger.critical(log_message)

    except ImportError:
        print("Error: pywin32 module not installed.")

def send_macos_logs(logger):
    try:
        process = subprocess.Popen(['log', 'show', '--last', '10m'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = process.communicate()
        log_messages = out.decode('utf-8').splitlines()

        for log_message in log_messages:
            print('macOS Log message before sending:', log_message)
            logger.critical(log_message)
    except FileNotFoundError:
        print("Error: 'log' command not found.")

def send_linux_logs(logger):
    try:
        process = subprocess.Popen(['journalctl', '--no-pager'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = process.communicate()
        log_messages = out.decode('utf-8').splitlines()

        for log_message in log_messages:
            print('Linux Log message before sending:', log_message)
            logger.critical(log_message)
    except FileNotFoundError:
        print("Error: 'journalctl' command not found. Using syslog alternative.")

        try:
            process = subprocess.Popen(['tail', '-n', '10', '/var/log/syslog'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, _ = process.communicate()
            log_messages = out.decode('utf-8').splitlines()

            for log_message in log_messages:
                print('Linux Log message before sending:', log_message)
                logger.critical(log_message)
        except FileNotFoundError:
            print("Error: 'tail' command not found.")

def send_memory_info(logger):
    # Collect and send memory information
    memory_info = psutil.virtual_memory()
    logger.info(f"Memory Usage: Total={memory_info.total}B, Available={memory_info.available}B, Used={memory_info.used}B, Percent={memory_info.percent}%")

def capture_network_logs(duration_seconds):
    try:
        file_path = 'network_logs.pcap'

        if platform.system() == 'Windows':
            subprocess.run(['netsh', 'trace', 'start', 'capture=yes', 'report=yes', 'filemode=single', 'maxsize=1024', 'fileprefix=netsh_log'], shell=True)
        elif platform.system() in ['Darwin', 'Linux']:
            subprocess.run(['sudo', 'tcpdump', '-w', file_path], stdout=subprocess.PIPE)

        time.sleep(duration_seconds)

        if platform.system() == 'Windows':
            subprocess.run(['netsh', 'trace', 'stop'], shell=True)
        elif platform.system() in ['Darwin', 'Linux']:
            subprocess.run(['sudo', 'killall', 'tcpdump'], stdout=subprocess.PIPE)

        print(f"Network logs saved to: {file_path}")

    except Exception as e:
        print(f"Error capturing network logs: {e}")

def extract_ips_from_csv(file_path, source_column, destination_column):
    ips = set()

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            source_ip = row.get(source_column, '')
            destination_ip = row.get(destination_column, '')

            # Extract IPs using a regular expression
            source_ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', source_ip)
            destination_ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', destination_ip)

            # Add the extracted IPs to the set
            ips.update(source_ips)
            ips.update(destination_ips)

    return list(ips)

# Example usage:
host = get_host_ip()
port = 9000
capture_duration = 60  # Capture logs for 60 seconds

logger, sh = setup_logger()

# Run the network and system logs capture functions in parallel
network_thread = threading.Thread(target=capture_network_logs, args=(capture_duration,))
network_thread.start()

system_thread = threading.Thread(target=send_system_logs_to_socket, args=(logger,))
system_thread.start()

# Wait for both threads to finish
network_thread.join()
system_thread.join()

# Replace 'network_logs.csv' with your actual network logs CSV file
network_logs_file = 'network_logs.csv'
source_column = 'SourceIP'
destination_column = 'DestinationIP'

extracted_ips = extract_ips_from_csv(network_logs_file, source_column, destination_column)
print("Extracted IPs from CSV:", extracted_ips)
