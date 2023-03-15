import openai

suggestions_boilerplate = "Describe your suggestion in pseudocode, written out in great detail. Be clear, but as concise as possible. List steps to take, but don't include actual code snippets. Make sure to avoid using fake libraries, 'example' URLs, URLs that do not provide the necessary data, dummy API key variables, or dummy data. Only use API keys if the user has given them to you, but don't ask for API keys. If you encounter any of these problems, change your approach. We want to make the code do what the user wants right out of the box!"

def generate_pseudocode_prompt(input):
	return f"How would you write a Python script that does the following:\n{input}\n{suggestions_boilerplate}"

def generate_error_instructions_prompt(input, prev_response, errors_list):
	return f"You previously produced a faulty response to the following prompt: 'Write Python code that solves the following challenge:\n{input}\nThe most recent faulty response was:\n'''\n{prev_response}\n'''\nThis faulty response produced the following error:\n'''{errors_list[-1]}\nHow would you fix this error while also avoiding previous errors? {suggestions_boilerplate}"

assistant_boilerplate = f"You are an AI programming assistant that gives coding instructions without writing actual code.\n\n- Follow the user's requirements carefully & to the letter.\n- First think step-by-step -- describe your plan for what to build in pseudocode, written out in great detail. Be clear, but as concise as possible. List steps to take, but don't include actual code snippets."

def generate_suggestions(prompt):
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": assistant_boilerplate},
			{"role": "user", "content": prompt}],
		max_tokens=3000,
		n=1,
		stop=None,
		temperature=0.7
	)
	# Extract the generated script from the API response
	response = response['choices'][0]['message']['content']
	return response