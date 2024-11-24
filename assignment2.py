#!/usr/bin/env python3
#Author: dnepal@myseneca.ca
'''For this assigment I am working on two different function, backup and restore.'''


import os
import tarfile

def data_backup(source_dir, backup_dir, archive_name):
    ''' This function backups the data from the provided filepath, compress it into .tar.gz and save it into the provided filepath backup directory'''

    if not os.path.isdir(source_dir): # checks if the source directory exists, if doesn't exists it gives a error message"
        print(f"Error: Source directory '{source_dir}' not found.")
        return None
    
    os.makedirs(backup_dir, exist_ok=True) # Checks if backup directory exists, if it doesn't exist it creates a new directory.

    archive_path = os.path.join(backup_dir, f"{archive_name}.tar.gz") # Full path for the archive

    with tarfile.open(archive_path, "w:gz") as tar: # Creates a compressed tar.gz archive of the specified source directory
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    
    print(f"Backup created at: {archive_path}") # Tells user that backup is completed sucessfully.
    return archive_path 
