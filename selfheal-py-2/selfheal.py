from suggest import generate_pseudo_code, generate_error_suggestions
from code import code_output, code_tests
from run import run

# Function that generates code from a user input. Returns the user_input, pseudo_code, code, and tests.
def generate_code(user_input):
    pseudo_code = generate_pseudo_code(user_input)
    output = code_output(user_input, pseudo_code)
    tests = code_tests(user_input, output)
    return user_input, pseudo_code, output, tests

# Function that runs the tests and uses any exceptions to generate suggestions and create new code and tests. Returns success/failure, new pseudo_code, new code, and new tests.
def test_iteration(user_input, pseudo_code, response, tests):
    test_results = run(tests)
    if test_results == None:
        tests_pass = True
        return tests_pass, pseudo_code, response, tests
    else:
        # Use test_results to generate suggestions and use those suggestions to generate new code and tests.
        tests_pass = False
        test_suggestions = generate_error_suggestions(user_input, response, tests, test_results)
        new_output = code_output(user_input, test_suggestions)
        new_tests = code_tests(user_input, new_output, test_results)
        # Return tests_pass, new pseudo_code, new code, and new tests.
        return tests_pass, test_suggestions, new_output, new_tests

def solve(user_input, max_fix_attempts=20):
    attempts_left = max_fix_attempts
    user_input, pseudo_code, output, tests = generate_code(user_input)
    print(f'\n\n\nAttempt:  {max_fix_attempts-attempts_left}\n\n------ pseudo_code ------\n{pseudo_code}\n\n------ output ------\n{output}\n------ tests ------\n{tests}\n------ test results ------\n{run(tests)}')
    tests_pass = test_iteration(user_input, pseudo_code, output, tests)[0]
    while tests_pass == False:
        tests_pass, pseudo_code, output, tests = test_iteration(user_input, pseudo_code, output, tests)
        print(f'\n\n\nAttempt:  {max_fix_attempts-attempts_left}\n\n------ pseudo_code ------\n{pseudo_code}\n\n------ output ------\n{output}\n------ tests ------\n{tests}\n------ test results ------\n{run(tests)}')
        if attempts_left == 0:
            raise Exception('max_fix_attempts has been reached. Try again or contact support.')
        attempts_left -= 1
    return pseudo_code, output, tests