#!/usr/bin/env python3
# Author: ashaikh38@myseneca.ca
'''This script  handles the error and create a log file .'''
import tarfile 

def handle_error(function, *args): # execute the provided function with the given arguments
    try:
        return function(*args) # Handle specific exceptions and log appropriate error messages
    except FileNotFoundError as e:
        log_error(e, "File or directory not found")
    except PermissionError as e:
        log_error(e, "Permission denied")
    except tarfile.ReadError as e:
        log_error(e, "Error reading tar.gz file")
    # Catch any other unexpected exceptions
    except Exception as e:
        log_error(e, "An unexpected error occurred")

def log_error(exception, message):
    '''
    Logs the error details to a file and informs the user
    '''
    
    log_file = "error_log.txt" # Specify the log file name
    # Open the log file in append mode to add new error details
    with open(log_file, "a") as log:
        log.write(f"{message}\n")  # Write the error message to the file
        log.write(f"Error details: {exception}\n")  # Log the exception details
        log.write("------\n")  # Separate this error log entry for clarity
    # Notify the user that an error occurred and point to the log file
    print(f"{message}. Check '{log_file}' for more details.") 
