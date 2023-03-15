import openai
import code_module


# Function that runs the code tests and returns the results
def run_tests(tests):
    # Run the tests
    try:
        exec(tests)
    except Exception as e:
        return e

# Function that runs the code and returns any terminal output or errors
def run_code(code):
    # Run the code
    try:
        exec(code)
    except Exception as e:
        return e