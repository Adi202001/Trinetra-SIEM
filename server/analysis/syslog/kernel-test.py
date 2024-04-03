import csv
from collections import defaultdict

def find_kernel_errors(file_name, verbose=False):
    kernel_errors = defaultdict(int)
    try:
        if verbose:
            print("Reading data from file:", file_name)
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                log_message = row['LogMessage']
                if "kernel:" in log_message.lower() and "error" in log_message.lower():
                    kernel_errors[log_message] += 1
        if verbose:
            print("Data processing complete.")
    except FileNotFoundError:
        print("Error: File not found:", file_name)
    except Exception as e:
        print("An error occurred:", e)
    return kernel_errors

# Example usage:
file_name = 'logs.csv'  # File name
verbose_mode = True  # Set to True for verbose mode, False otherwise
kernel_errors = find_kernel_errors(file_name, verbose=verbose_mode)
print("Kernel errors found:")
for error, count in kernel_errors.items():
    print("Error:", error, "- Occurrences:", count)
