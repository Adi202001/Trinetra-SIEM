import os
import socket
import logging
import logging.handlers
import pickle
import csv
import threading
import json  # Alternative serialization
import time
import subprocess

def receive_log_from_client(client_socket, csv_files, chunk_size=4096):
    try:
        total_data = b''
        while True:
            chunk = client_socket.recv(chunk_size)
            if not chunk:
                break  # Client socket closed
            total_data += chunk
        # Process received data and write to CSV in streaming mode
        records = deserialize_data(total_data)
        for record in records:
            system = record.get('System', 'Unknown')
            csv_writer = csv_files.get(system)
            if csv_writer:
                del record['System']  # Remove system information before writing to CSV
                csv_writer.writerow(record)
    except socket.error as e:
        print(f"Socket error with client {client_socket.getpeername()}: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        client_socket.close()

def receive_pcap_data(host, port):
    try:
        process = subprocess.Popen(['tcpdump', '-w', '-', '-U', '-n', '-i', 'eth0'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((host, port))
            sock.listen(5)
            while True:
                conn, addr = sock.accept()
                print(f"Received connection from {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    process.stdin.write(data)
    except Exception as e:
        print(f"Error receiving pcap data: {e}")
    finally:
        process.terminate()

def deserialize_data(data):
    try:
        if b'json:' in data[:5]:  # Check for JSON signature
            return json.loads(data[5:])
        else:
            return pickle.loads(data)
    except (json.JSONDecodeError, pickle.PickleError) as e:
        print(f"Error deserializing data: {e}")
        return []

def receive_logs_and_save_to_csv(host, port, systems):
    logger = logging.getLogger('receiver_logger')
    sh = logging.handlers.SocketHandler(host, port)
    sh.protocol = socket.SOCK_STREAM  # Set protocol explicitly
    logger.addHandler(sh)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    csv_files = {}
    for system in systems:
        csv_path = os.path.join(script_dir, f'{system.lower()}_logs.csv')
        with open(csv_path, 'a+', newline='') as csvfile:
            fieldnames = ['LineId', 'Month', 'Date', 'Time', 'Level', 'Component', 'PID', 'Content', 'EventId']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                csv_writer.writeheader()
            csv_files[system] = csv_writer

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    try:
        while True:
            (client_socket, client_address) = server_socket.accept()
            print(f"Client connected from {client_address}")
            thread = threading.Thread(target=receive_log_from_client, args=(client_socket, csv_files))
            thread.start()
    except KeyboardInterrupt:
        pass
    finally:
        for csv_writer in csv_files.values():
            csv_writer.file.close()
        logger.removeHandler(sh)
        sh.close()

def get_ipv4_address():
    s = None  # Initialize the socket object outside the try block
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to a remote server (doesn't actually send any data)
        s.connect(("8.8.8.8", 80))

        # Get the local IP address
        ipv4_address = s.getsockname()[0]

        return ipv4_address
    except socket.error as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        if s:  # Check if the socket object is created
            s.close()  # Close the socket if it's not None

if __name__ == "__main__":
    host = get_ipv4_address()
    if host:
        port = 9000
        pcap_port = 9003
        systems = ['Windows', 'MacOS', 'Linux']  # Define systems for classification
        receive_logs_and_save_to_csv(host, port, systems)
        receive_pcap_data(host, pcap_port)
    else:
        print("Unable to retrieve IPv4 address.")
