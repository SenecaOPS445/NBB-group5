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