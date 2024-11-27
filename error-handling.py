def handle_error(exception, message="An error occurred"):
    '''
    This function handles errors by logging the details to a file
    and showing a simple message to the user.

    Parameters:
    - exception: The error that was caught.
    - message: A short message explaining the error.
    '''
    log_file = "error_log.txt"  # Name of the error log file
    with open(log_file, "a") as file:  # Open the log file in append mode
        file.write(f"{message}\n")
        file.write(f"Error Details: {exception}\n")
        file.write("------\n")
    print(f"{message}. Check '{log_file}' for more details.")  # Notify the user