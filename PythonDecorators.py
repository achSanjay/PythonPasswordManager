def log_message(func):
    def wrapper(*args, **kwargs):
        # Call the decorated function
        result = func(*args, **kwargs)
        # Open the log file in append mode
        with open('/tmp/decorator_logs.txt', 'a') as f:
            # Write the result to the file as a new line
            f.write(result + '\n')
        # Return the result as usual
        return result
    return wrapper

# Example usage
@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"
