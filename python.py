
import json
import re
from pathlib import Path

def extract_error_logs(log_file_path, output_file_path):
    """
    Extracts error log entries with timestamps from a log file and saves them to a JSON file.

    Args:
        log_file_path (str or Path): The path to the log file.
        output_file_path (str or Path): The path to the output JSON file.
    """
    log_file_path = Path(log_file_path) # Convert to path object
    output_file_path = Path(output_file_path) # Convert to path object
    error_data = []

    try:
        with open(log_file_path, 'r') as log_file:
            log_file_content = log_file.read()

            # More robust pattern
            error_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})\s*-\s*ERROR\s*-\s*(.*?)(?=\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}|\Z)"
            matches = re.findall(error_pattern, log_file_content, re.DOTALL)

            for match in matches:
                timestamp = match[0]
                error_message = match[1].strip()
                error_data.append({'timestamp': timestamp, 'error_message': error_message})

        with open(output_file_path, 'w') as json_file:
            json.dump(error_data, json_file, indent=4)  # indent for pretty printing

        print(f"Successfully extracted error data and saved to {output_file_path}")

    except OSError as e:
        print(f"Error: File access problem: {e}")
    except json.JSONDecodeError as e:
         print(f"Error: json.JSONDecodeError {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
log_file_path = 'C:\\Users\\290419\\Desktop\\exam\\timestamp.log'
output_file_path = 'output.json'
extract_error_logs(log_file_path, output_file_path)

