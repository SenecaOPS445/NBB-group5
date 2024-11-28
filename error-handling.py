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
    
    try:
        return function(*args)  
    except FileNotFoundError as e:
        log_error(e, "File or directory not found") 
    except PermissionError as e:
        log_error(e, "Permission denied") 
    except tarfile.ReadError as e:
        log_error(e, "Error reading tar.gz file")
    except Exception as e:
        log_error(e, "An unexpected error occurred")



def log_error(exception, message):
    '''
    Logs the error details to a file and informs the user
    '''
    log_file = "error_log.txt"
    with open(log_file, "a") as log:
        log.write(f"{message}\n")
        log.write(f"Error details: {exception}\n")
        log.write("------\n")
    print(f"{message}. Check '{log_file}' for more details.")



if __name__ == "__main__":
    source_dir = "/home/ashaikh38/data_source"
    backup_dir = "/home/ashaikh38/backup"    
    archive_name = "backup"                  
    archive_path = "/home/ashaikh38/backup/backup.tar.gz" 
    restore_dir = "/home/ashaikh38/restore"    


    # Test backup process
    print("\n--- Backup Process ---")
    handle_error(data_backup, source_dir, backup_dir, archive_name)

    # Test restore process
    print("\n--- Restore Process ---")
    handle_error(data_restore, archive_path, restore_dir)
