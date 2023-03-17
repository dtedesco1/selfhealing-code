import os
from suggest import generate_inputs, generate_name
from run import run
import selfheal

def main():
    # user_input = generate_inputs()
    user_input = "Use the Wikipedia API to search for the most popular tourist attractions in Paris, France. Display the top 5 results along with a brief description and a thumbnail image in the terminal."
    print(user_input)
    pseudo_code, output, tests = selfheal.solve(user_input, 10)

    # Run the solved code.
    run(output)

    # Store the pseudo_code, output, and tests in separate files in a new subdirectory.
    # Generate a name for the subdirectory based on the first few words of the user_input.
    name = generate_name(user_input)
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
    
    # Delete the temporary files.
    os.remove('output.py')
    os.remove('tests.py')

if __name__ == "__main__":
    main()