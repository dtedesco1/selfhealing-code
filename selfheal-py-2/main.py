from suggest import generate_inputs, generate_name
from local import run, store_solutions
import selfheal

def main():

    # Prompt generator
    # user_input = generate_inputs()

    # Ask the user for a task.
    user_input = input('What would you like to do? ')

    print(user_input)

    # Solve the user_input.
    pseudo_code, output, tests = selfheal.solve(user_input, 10)

    # Run the solved code.
    run(output)

    # Generate a name for the subdirectory based on the first few words of the user_input.
    name = generate_name(user_input)
    print(name)

    # Store the pseudo_code, output, and tests in separate files in a new subdirectory.
    store_solutions(name, user_input, pseudo_code, output, tests)

if __name__ == "__main__":
    main()