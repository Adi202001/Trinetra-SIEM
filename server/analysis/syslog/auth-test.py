import csv
from collections import defaultdict
from datetime import datetime

def find_authentication_failures(file_name, verbose=False):
    authentication_failures = defaultdict(int)
    try:
        if verbose:
            print("Reading data from file:", file_name)
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                timestamp_epoch = float(row['Timestamp'])
                timestamp = datetime.utcfromtimestamp(timestamp_epoch).strftime('%Y-%m-%d %H:%M:%S')
                log_message = row['LogMessage']
                if verbose:
                    print("Processing row - Timestamp:", timestamp, "- LogMessage:", log_message)
                if "authentication failure" in log_message.lower():
                    minute_key = datetime.utcfromtimestamp(timestamp_epoch).strftime('%Y-%m-%d %H:%M')
                    authentication_failures[minute_key] += 1
        if verbose:
            print("Data processing complete.")
    except FileNotFoundError:
        print("Error: File not found:", file_name)
    except Exception as e:
        print("An error occurred:", e)
    excessive_failures = {minute: count for minute, count in authentication_failures.items() if count > 5}
    return excessive_failures

# Example usage:
file_name = 'logs.csv'  # File name
verbose_mode = True  # Set to True for verbose mode, False otherwise
excessive_failures = find_authentication_failures(file_name, verbose=verbose_mode)
print("Minutes with more than 5 authentication failures:")
for minute, count in excessive_failures.items():
    print("Minute:", minute, "- Authentication Failures:", count)
