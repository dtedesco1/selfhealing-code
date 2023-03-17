from suggest import generate_inputs, generate_name
from local import run, store_solutions
import selfheal

def main():
    # user_input = generate_inputs()
    # user_input = "Use the Wikipedia API to search for the most popular tourist attractions in Paris, France. Display the top 5 results along with a brief description in the terminal."
    # user_input = "Monitor the International Space Station's (ISS) location in real time and display its position relative to my current location on Earth."
    user_input = "Display one of today's top cat memes in the terminal."
    print(user_input)

    # Solve the user_input.
    pseudo_code, output, tests = selfheal.solve(user_input, 10)

    # Run the solved code.
    run(output)

    # Generate a name for the subdirectory based on the first few words of the user_input.
    name = generate_name(user_input)

    # Store the pseudo_code, output, and tests in separate files in a new subdirectory.
    store_solutions(name, user_input, pseudo_code, output, tests)

    # Delete the temporary files.
    import os
    os.remove('output.py')
    os.remove('tests.py')

if __name__ == "__main__":
    main()