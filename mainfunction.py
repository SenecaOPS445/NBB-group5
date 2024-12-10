#!/usr/bin/env python3
#Author ID : msoufi1

from errorhandling import handle_error

'''
For this assignmentm I am working on the main block. for backup and restore.
'''

import sys
def print_usage():
    '''Prints the usage instructions for the script.'''
    print("Usage:")
    print(" To backup: check.py backup <source_dir> <backup_dir> <archive_name>")
    print(" To restore: check.py restore <archive_path> <restore_dir>")

def main():
    '''Main function to handle command-line arguments and execute backup or restore.'''
    if len(sys.argv) < 2:                                                                     #check argument that its 2 arguemnt if not give errro message
        print("Error: Insufficient arguments provided.")
        print_usage()
        sys.exit(1)

    operation = sys.argv[1].lower()                                                        # Convert operation like Backup too all lower case, or Restore to avoid case senetvity problems 
 
    if operation == "backup":                                                              # Make sure opertuion for backup is 5 arguments, Script name, operation, source directory, backup directory, and archive name, if not give error
        if len(sys.argv) != 5: 
            print("Error: Incorrect arguments for backup.")
            print_usage()
            sys.exit(1)

        source_dir = sys.argv[2]
        backup_dir = sys.argv[3]
        archive_name = sys.argv[4]

       
 
        print("\n--- Backup Process ---")                                                  # Handle_error wrapper likely ensures any errors during the backup
        handle_error(data_backup, source_dir, backup_dir, archive_name)

    elif operation == "restore":                                                           # Make sure opertuion for restore is 4 arguments, Script name, operation, archive path, and restore directory. if not give error
        if len(sys.argv) != 4:                                                             
            print("Error: Incorrect arguments for restore.")
            print_usage()
            sys.exit(1)

        archive_path = sys.argv[2]
        restore_dir = sys.argv[3]

        

        print("\n--- Restore Process ---")
        handle_error(data_restore, archive_path, restore_dir)                             # The handle_error wrapper ensures any errors are caught and reported.

    else:
        print(f"Error: Unknown operation '{operation}'.")                                #Tells us invalid operations anything other than backup or restore. Prints an error message and exits.
        print_usage()
        sys.exit(1)

if __name__ == "__main__":
    main()




    
