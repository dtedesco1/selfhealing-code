from suggest import generate_pseudo_code, generate_error_suggestions
from gen_code import code_output, code_tests
from local import run, run_tests

# Function that generates code from a user input. Returns the user_input, pseudo_code, code, and tests.
def generate_code(user_input):
    pseudo_code = generate_pseudo_code(user_input)
    output = code_output(user_input, pseudo_code)
    tests = code_tests(user_input, output)
    return user_input, pseudo_code, output, tests

# Function that runs the tests and uses any exceptions to generate suggestions and create new code and tests. Returns success/failure, new suggestions, new code, and new tests.
def iteration(user_input, suggestions, output, tests):
    # Run the tests. If they pass, run the code. If they fail, generate suggestions and use those suggestions to generate new code and tests.
    try:
        test_errors = run_tests(tests)
        if test_errors == None:
            print('passing')
            run(output)
        else:
            no_errors = False
            suggestions = generate_error_suggestions(user_input, output, tests, test_errors)
            output = code_output(user_input, suggestions)
            tests = code_tests(user_input, output, test_errors)
            return no_errors, suggestions, output, tests
    except Exception as e:
        no_errors = False
        # Use e to generate suggestions and use those suggestions to generate new code and tests.
        code_suggestions = generate_error_suggestions(user_input, output, tests, e)
        new_output = code_output(user_input, code_suggestions)
        new_tests = code_tests(user_input, new_output)
        return no_errors, code_suggestions, new_output, new_tests
    finally:
        no_errors = True
        return no_errors, suggestions, output, tests

# Function that runs the code and tests and keeps trying to fix the code until the tests pass.
def solve(user_input, max_fix_attempts=20):
    attempts_left = max_fix_attempts
    user_input, suggestions, output, tests = generate_code(user_input)
    print(f'\n\n\nAttempt:  {max_fix_attempts-attempts_left}\n\n\n\n------ suggestions ------\n\n\n\n{suggestions}\n\n\n\n------ output ------\n{output}\n\n\n\n------ tests ------\n{tests}\n\n\n\n------ code output ------\n{run(output)}')
    no_errors = iteration(user_input, suggestions, output, tests)[0]

    # While the tests don't pass, keep trying to fix the code.
    while no_errors == False:
        no_errors, suggestions, output, tests = iteration(user_input, suggestions, output, tests)
        print(f'\n\n\nAttempt number:  {max_fix_attempts-attempts_left}\n\n\n\n------ suggestions ------\n\n\n\n{suggestions}\n\n\n\n------ output ------\n{output}\n\n\n\n------ tests ------\n{tests}\n\n\n\n------ code output ------\n{run(output)}')
        if attempts_left == 0:
            raise Exception('max_fix_attempts has been reached. Try again or contact support.')
        attempts_left -= 1
        print(f'Attempts left: {attempts_left}')

    return suggestions, output, tests