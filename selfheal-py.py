import openai
import os
import re

# Set the OpenAI API key
# openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = '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' # This is a test key. Please use your own key.

# Define the function to generate the python code
def generate_code(user_input):
    # Send the user input to GPT-3 to generate the script
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a bot that responds with only working, errorless Python code and nothing else."},
            {"role": "user", "content": "Write Python code that solves the following challenge:\nPrint the word 'foobar'\n\nDO NOT explain what you're doing in natural language. DO NOT use a codeblock. ONLY respond with code. Your code:"},
            {"role": "assistant", "content": "print('foobar')"},
            {"role": "user", "content": "Perfect! Thank you. Let's try another."},
            {"role": "user", "content": f"Write Python code that solves the following challenge:\n{user_input}\n\nDO NOT explain what you're doing in natural language. DO NOT use a codeblock. ONLY respond with code. Your code:"}],
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.7
    )
    # Extract the generated script from the API response
    response = response['choices'][0]['message']['content']
    return response



# Define the function to run the generated code
def run_code(code):
    exec(code)

# Define the function to fix errors using GPT-3
def fix_error(prev_response, errors_list, attempt_num, max_attempts):
    if attempt_num >= max_attempts:
        raise Exception("Max number of fix attempts reached. Please fix the error manually.")
    prompt = f"ChatGPT has produced a faulty response to the following prompt: 'Write Python code that does the following:\n{user_input}\ChatGPT's most recent response to the prompt is:\n'''\n{prev_response}\n'''\nPrevious attempts received the following errors when run:\n'''{errors_list}'''\nCan you generate a new response so that it meets the goal of its prompt and avoids all the errors? DO NOT make the same errors that have been made before. Be creative to find new solutions. DO NOT explain what you're doing in natural language. DO NOT use a codeblock. ONLY respond with code. Your Python code:"
    # Send the error message to GPT-3
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a bot that responds with only working, errorless Python code and nothing else. You are also a bot that can fix errors in other bots' code. Don't produce code that repeats the same errors as the past!"},
            {"role": "user", "content": "Write Python code that solves the following challenge:\nPrint the word 'foobar'\nYour code:"},
            {"role": "assistant", "content": "print('foobar')"},
            {"role": "user", "content": "Perfect! Thank you. Let's try another."},
            {"role": "user", "content": "Write Python code that solves the following challenge:\nPrint the numbers 1 through 10'\nYour code:"},
            {"role": "assistant", "content": "print('def print_numbers():\n    for i in range(1, 11):\n        print(i)')"},
            {"role": "user", "content": "Perfect! Thank you. Let's try another."},
            {"role": "user", "content": prompt}],
        max_tokens=3000,
        n=5,
        stop=None,
        temperature=0.7
    )
    response = response['choices'][0]['message']['content']
    if not response:
        raise Exception("Could not find a solution to the error. Please fix it manually.")
    return response

# Define the main function to run the first script
def main():
    global user_input
    user_input = input("Please enter what you would like the Python script to do: ")
    # user_input = "Print the numbers 1 to 10"
    # user_input = "Print a fibonacci sequence up to 10, but add a unique line of poetry after each number. Make each line of poetry refer to the number in the sequence with which it's associated.""
    # user_input = "In the terminal, print ASCII characters in the image of a cat's head."
    # user_input = "Print a pattern of asterisks that looks like a Christmas tree."
    # user_input = "Generate a mathematical function whose results look like a flower when printed in the terminal. Print those results in the terminal."
    # user_input = "Generate a mathematical function whose results look like a spiral galaxy when printed in the terminal. Print those results in the terminal."
    # user_input = "Use web scraping to find the current weather in Philadelphia, Pennsylvania. Print the results in the terminal."
    # user_input = "Find the latest price of Ethereum online. Print the results in the terminal."
    # user_input = "Find an image of the current weather in Philadelphia, Pennsylvania. Store the image and the script you used to generate it in the locally."
    # user_input = "Find online the total value of the top 10 cryptocurrencies using a tool like Beautiful Soup. Display a histogram of the data using 3 buckets."
    user_input = "Get monthly unemployment rate data in the U.S. from https://data.bls.gov/timeseries/LNS14000000. Parse the table and print the data for December 2022 in the terminal."
    new_response = generate_code(user_input)
    errors_list=[]
    max_fix_attempts = 20
    fix_attempt = 0
    while True:
        print(f'## Running script:\n{new_response}\n## End of Script ##')
        try:
            run_code(new_response)
        except Exception as e:
            error_msg = str(e)
            errors_list.append(error_msg)
            fix_attempt += 1
            print(f"## Fix attempt {fix_attempt}/{max_fix_attempts} ##\n## Error message: {error_msg} ##")
            try:
                old_response = new_response
                new_response = fix_error(old_response, errors_list, fix_attempt, max_fix_attempts)
            except Exception as e:
                print(str(e))
                break
        else:
            break
    print(errors_list)

# Call the main function to start the process
main()