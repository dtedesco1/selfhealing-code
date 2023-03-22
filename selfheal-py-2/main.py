from suggest import generate_inputs, generate_name
from local import run, store_solutions
import selfheal

def main():
    # user_input = generate_inputs()
    # user_input = "Use the Wikipedia API to search for the most popular tourist attractions in Paris, France. Display the top 5 results along with a brief description in the terminal."
    # user_input = "Monitor the International Space Station's (ISS) location in real time and display its position relative to my current location on Earth."
    # user_input = "Use very concise code to draw a blue circle inside of a light blue square and save it locally."
    # user_input = "Download and store locally one real cat meme. Don't use APIs."
    # user_input = "What's the most recent tweet from Elon Musk? Don't use APIs."
    user_input = "Make a histogram of the number of times each of the top 10 words appear in the text of the Wikipedia page for the Olympics. Store the histogram locally."
    # user_input = "Count the number of times the word 'the' appears in the text of the Wikipedia page for the International Space Station."
    # user_input = "Find an image of the current weather in Philadelphia, Pennsylvania. Store the image and the script you used to generate it in the locally."
    # user_input = "Write a python script to solve the following without the need for any API keys: Find an image of the current weather in Philadelphia, Pennsylvania. Store the image locally."

    # Ask the user for a task.
    # user_input = input('What would you like to do? ')

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