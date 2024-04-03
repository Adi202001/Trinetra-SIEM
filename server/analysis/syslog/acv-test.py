import csv
from collections import defaultdict

def find_access_control_violations(file_name, verbose=False):
    access_control_violations = defaultdict(int)
    try:
        if verbose:
            print("Reading data from file:", file_name)
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                log_message = row['LogMessage']
                if "access control violation" in log_message.lower():
                    access_control_violations[log_message] += 1
        if verbose:
            print("Data processing complete.")
    except FileNotFoundError:
        print("Error: File not found:", file_name)
    except Exception as e:
        print("An error occurred:", e)
    return access_control_violations

# Example usage:
file_name = 'logs.csv'  # File name
verbose_mode = True  # Set to True for verbose mode, False otherwise
access_control_violations = find_access_control_violations(file_name, verbose=verbose_mode)
print("Access control violations found:")
for violation, count in access_control_violations.items():
    print("Violation:", violation, "- Occurrences:", count)
