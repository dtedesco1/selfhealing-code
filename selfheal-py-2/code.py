from config import openai, model
import os

code_prompt_boilerplate = "\nDO NOT explain what you're doing in natural language. DO NOT use a codeblock. ONLY respond with code. Make sure to avoid using 'example' URLs, URLs that do not provide the necessary data, or dummy API key or other configuration variables. Only use API keys if the user has given them to you in the prompt. If an API key is not part of the prompt, DO NOT REQUIRE API KEYS IN YOUR CODE. If you encounter any of these, change your approach and, if necessary, your data source. We want to make the code do what the user wants right out of the box! Assume NO external libraries have been installed previously. If you need any libraries, write a function to install them in the local environment."

# Define the function to generate python code based on a prompt
def code(prompt):
	# Send the user input to the model to generate a script
	response = openai.ChatCompletion.create(
		model=model,
		messages=[
			{"role": "system", "content": "You are a bot that responds to prompts with only working, errorless Python code and nothing else. Your outputs can be pasted directly into a Python file and run."},
			{"role": "user", "content": "Write Python code that meets the following user need:\nPrint the word 'foobar'\nYour code:"},
			{"role": "assistant", "content": "print('foobar')"},
			{"role": "user", "content": "Perfect! Thank you. Let's try another."},
			{"role": "user", "content": "Write Python code that meets the following user need:\nPrint the numbers 1 through 10'\nYour code:"},
			{"role": "assistant", "content": "print('def print_numbers():\n    for i in range(1, 11):\n        print(i)')"},
			{"role": "user", "content": "Perfect! Thank you. Let's try another."},
			{"role": "user", "content": prompt,}],
		max_tokens=3000,
		n=1,
		stop=None,
		temperature=0.7
	)
	# Extract the generated script from the API response
	response = response['choices'][0]['message']['content']
	return response

# Function to generate the code prompt and generate the code.
def code_output(input, suggestions):
	prompt = f"Write Python code that meets the following user need:\n{input}\n\nPlease follow these suggestions:\n{suggestions}\n{code_prompt_boilerplate}. Your code will be stored in the local directory as 'output.py'. Your code:"
	output = code(prompt)
	with open("output.py", "w") as f:
		f.write(output)
	return output

# Function to generate the tests prompt and generate the tests.
def code_tests(input, output, test_results=None):
	# generate a prompt asking the AI to write tests for the code to ensure it meets the user's needs
	prompt = f"Write tests for the following code (stored in the local directory as 'output.py'):\n{output}\n\nThe code should meet the following user need:\n{input}\n{code_prompt_boilerplate}. Your test code will be stored at in the local directory as 'tests.py'. Your previous test failed with the following error:\n{test_results}\nEnsure your new test code itself is not buggy. If you need external libraries, you might need to install them yourself inside the test code. Your test code:"
	tests = code(prompt)
	with open("tests.py", "w") as f:
		f.write(tests)
	return tests