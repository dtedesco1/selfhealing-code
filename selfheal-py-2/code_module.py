import openai

code_generation_boilerplate = "\nDO NOT explain what you're doing in natural language. DO NOT use a codeblock. ONLY respond with code. Make sure to avoid using fake libraries, 'example' URLs, URLs that do not provide the necessary data, dummy API key variables, or dummy data. Only use API keys if the user has given them to you. If you encounter any of these, change your approach and, if necessary, your data source. We want to make the code do what the user wants right out of the box!"

def generate_code_prompt(input, suggestions):
	prompt = f"Write Python code that meets the following user need:\n{input}\n\nPlease follow these suggestions:\n{suggestions}\n{code_generation_boilerplate} Your code:"
	return prompt

def generate_tests_prompt(input, code):
	# generate a prompt asking the AI to write tests for the code to ensure it meets the user's needs
	prompt = f"Write tests for the following code:\n{code}\n\nThe code should meet the following user need:\n{input}\n{code_generation_boilerplate} Your test code:"


# Define the function to generate the python code
def generate_code(prompt):
	# Send the user input to GPT-3 to generate the script
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "You are a bot that responds with only working, errorless Python code and nothing else. Your outputs can be pasted directly into a Python file and run."},
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

# Define the function to run the generated code
def run_code(code):
	exec(code)