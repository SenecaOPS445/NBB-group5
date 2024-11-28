#!/usr/bin/env python3
# Author: ashaikh38@myseneca.ca
'''This script provides functions for data backup and restoration, along with error handling.'''

import os
import tarfile

# Backup function
def data_backup(source_dir, backup_dir, archive_name):
    if not os.path.isdir(source_dir):  
        print(f"Error: Source directory '{source_dir}' not found.")
        return None

    os.makedirs(backup_dir, exist_ok=True)  
    archive_path = os.path.join(backup_dir, f"{archive_name}.tar.gz")  

    with tarfile.open(archive_path, "w:gz") as tar:  
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    print(f"Backup created at: {archive_path}")  
    return archive_path


# Restore function
def data_restore(archive_path, restore_dir):
    os.makedirs(restore_dir, exist_ok=True)  

    with tarfile.open(archive_path, "r:gz") as tar:  
        tar.extractall(path=restore_dir)

    print(f"Data restored to: {restore_dir}")  
    return restore_dir


# Error-handling function
def handle_error(function, *args):
    '''
    Executes the given function and handles any errors that occur.

    Parameters:
    - function: The function to execute.
    - *args: Arguments to pass to the function.

    Returns:
    - The result of the function if successful.
    - None if an error occurs.
    '''
    try:
        return function(*args)  # Attempt to execute the provided function
    except FileNotFoundError as e:
        log_error(e, "File or directory not found")  # Handle file not found errors
    except PermissionError as e:
        log_error(e, "Permission denied")  # Handle permission errors
    except tarfile.ReadError as e:
        log_error(e, "Error reading tar.gz file")  # Handle issues with the archive file
    except Exception as e:
        log_error(e, "An unexpected error occurred")  # Handle other unexpected errors


# Function to log errors
def log_error(exception, message):
    '''
    Logs the error details to a file and informs the user.

    Parameters:
    - exception: The error that occurred.
    - message: A user-friendly description of the error.
    '''
    log_file = "error_log.txt"  # Log file to store error details
    with open(log_file, "a") as log:  # Open the log file in append mode
        log.write(f"{message}\n")  # Log a user-friendly message
        log.write(f"Error details: {exception}\n")  # Log technical details
        log.write("------\n")
    print(f"{message}. Check '{log_file}' for more details.")  # Notify the user about the log


# Main block for testing the functionality
if __name__ == "__main__":
    # Paths for testing (replace these with actual paths during testing)
    source_dir = "/home/ashaikh38/data_source"  # Example of an existing directory
    backup_dir = "/home/ashaikh38/backup"      # Directory for the backup
    archive_name = "backup"                    # Name of the archive file
    archive_path = "/home/ashaikh38/backup/backup.tar.gz"  # Path to the archive
    restore_dir = "/home/ashaikh38/restore"    # Directory to restore data


    # Test backup process
    print("\n--- Backup Process ---")
    handle_error(data_backup, source_dir, backup_dir, archive_name)

    # Test restore process
    print("\n--- Restore Process ---")
    handle_error(data_restore, archive_path, restore_dir)
