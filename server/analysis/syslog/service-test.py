import csv
from collections import defaultdict

def find_service_errors(file_name, verbose=False):
    service_errors = defaultdict(int)
    try:
        if verbose:
            print("Reading data from file:", file_name)
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                log_message = row['LogMessage']
                if "failed to start" in log_message.lower():
                    service_name = extract_service_name(log_message)
                    if service_name:
                        service_errors[service_name] += 1
        if verbose:
            print("Data processing complete.")
    except FileNotFoundError:
        print("Error: File not found:", file_name)
    except Exception as e:
        print("An error occurred:", e)
    return service_errors

def extract_service_name(log_message):
    start_index = log_message.find("Failed to start ")
    if start_index != -1:
        end_index = log_message.find(":", start_index)
        if end_index != -1:
            return log_message[start_index + len("Failed to start "):end_index]
    return None

# Example usage:
file_name = 'logs.csv'  # File name
verbose_mode = True  # Set to True for verbose mode, False otherwise
service_errors = find_service_errors(file_name, verbose=verbose_mode)
print("Service errors found:")
for service, count in service_errors.items():
    print("Service:", service, "- Error count:", count)
