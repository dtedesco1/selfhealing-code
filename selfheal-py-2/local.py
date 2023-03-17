import os

# Run a command line command to run the tests and store their results in a text file.
def run_tests(tests):
    if run(tests) == None:
        # Delete the text file
        os.remove('test_results.txt')
        return None
    else:
        os.system("python3 -m unittest tests.py > test_results.txt 2>&1")
        # open the text file and read the results
        with open('test_results.txt', 'r') as f:
            results = f.read()
        return results

# Function that runs code and returns exceptions
def run(code):
    # Run the file
    try:
        exec(code)
    except Exception as e:
        return e
    else:
        return None

# Store the pseudo_code, output, and tests in separate files in a new subdirectory.
def store_solutions(name, user_input, pseudo_code, output, tests):
    # First, create the subdirectory if it doesn't exist already. If it exists, raise an error.
    if os.path.exists(f'solved/{name}'):
        raise Exception('The directory already exists.')
    os.mkdir(f'solved/{name}')
    # Then, create the files and write the code to them.
    with open(f'solved/{name}/input.txt', 'w') as f:
        f.write(user_input)
    with open(f'solved/{name}/pseudo_code.txt', 'w') as f:
        f.write(pseudo_code)
    with open(f'solved/{name}/output.py', 'w') as f:
        f.write(output)
    with open(f'solved/{name}/tests.py', 'w') as f:
        f.write(tests)