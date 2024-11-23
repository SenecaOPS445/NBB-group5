#!/usr/bin/env python3
#Author: dnepal@myseneca.ca
'''For this assigment I am working on two different function, backup and restore.'''


import os
import tarfile

def data_backup(source_dir, backup_dir, archive_name):
    ''' This function backups the data from the provided filepath, compress it into .tar.gz and save it into the provided filepath backup directory'''

    
