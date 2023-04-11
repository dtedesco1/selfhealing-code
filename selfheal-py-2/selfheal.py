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
def iteration(user_input, suggestions, output):
    tests = 'No tests created as this time.'
    # Run the tests. If they pass, run the code. If they fail, generate suggestions and use those suggestions to generate new code and tests.
    try:
        run(output)
        tests = code_tests(user_input, output, test_errors)
        print(f'\n##### Tests #####\n{tests}\n\n')
        test_errors = run_tests(tests)
        print(f'\n##### Test Errors #####\n{test_errors}\n\n')
        if test_errors == None:
            print(f'\nTests passed!\n\n')
        else:
            no_errors = False
            suggestions = generate_error_suggestions(user_input, output, tests, test_errors)
            print(f'\n##### Suggestions #####\n{suggestions}\n\n')
            output = code_output(user_input, suggestions)
            print(f'\n##### New Code #####\n{output}\n\n')
            return no_errors, suggestions, output
    except Exception as e:
        no_errors = False
        # Use e to generate suggestions and use those suggestions to generate new code and tests.
        code_suggestions = generate_error_suggestions(user_input, output, tests, e)
        print(f'\n##### Suggestions #####\n{code_suggestions}\n\n')
        new_output = code_output(user_input, code_suggestions)
        print(f'\n##### New Code #####\n{new_output}\n\n')
        return no_errors, code_suggestions, new_output, tests
    else:
        no_errors = True
        print(f'\nNo errors found!\n\n')
        return no_errors, suggestions, output, tests

# Function that runs the code and tests and keeps trying to fix the code until the tests pass.
def solve(user_input, max_fix_attempts=20):
    attempts_left = max_fix_attempts
    print(f'\n##### Attempts Left #####\n{attempts_left}\n\n')
    user_input, suggestions, output, tests = generate_code(user_input)
    # print(f'\n\n\nAttempt:  {max_fix_attempts-attempts_left}\n\n\n\n------ suggestions ------\n\n\n\n{suggestions}\n\n\n\n------ code output ------\n{run(output)}')
    no_errors = iteration(user_input, suggestions, output)[0]

    # While the tests don't pass, keep trying to fix the code.
    while no_errors == False:
        no_errors, suggestions, output, tests = iteration(user_input, suggestions, output)
        # print(f'\n\n\nAttempt number:  {max_fix_attempts-attempts_left}\n\n\n\n------ suggestions ------\n\n\n\n{suggestions}\n\n\n\n------ code output ------\n{run(output)}')
        if attempts_left == 0:
            raise Exception('max_fix_attempts has been reached. Try again or contact support.')
        attempts_left -= 1
        print(f'Attempts left: {attempts_left}')

    return suggestions, output, tests