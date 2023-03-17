from config import openai, model

assistant_boilerplate = f"You are an AI programming assistant that gives coding suggestions and instructions without writing all the code yourself.\n\n- Follow the user's requirements carefully & to the letter.\n- First think step-by-step -- describe your plan for what to build in pseudocode, written out in great detail. Be clear. List steps to take, but use natural language to explain yourself rather than writing actual code. Explain your reasoning and make suggestions so another AI like yourself can understand."

def generate_suggestions(prompt):
	response = openai.ChatCompletion.create(
		model=model,
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

def generate_inputs():
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a bot that generates interesting coding challenges for other AI to develop working code for. You are not allowed to write code yourself. You can only generate prompts for other AI to write code for."},
            {"role": "user", "content": "Please come up with an interesting coding challenge for another AI to solve you describe in a short prompt. Previous good examples include:\n- 'Find an image of the current weather in Philadelphia, Pennsylvania. Store the image and the script you used to generate it in the locally.'\n- 'I want to know the current total value of the top 10 cryptocurrencies. Can you find and show each of the top ten to me in the terminal?' Can you come up with a new challenge? Be creative! Make sure they are not too easy or too hard, and that they can be reasonably completed with 3000 tokens."},
            {"role": "assistant", "content": "Get monthly unemployment rate data in the U.S. from https://data.bls.gov/timeseries/LNS14000000. Parse the table and print the data for 2022 in the terminal."},
            {"role": "user", "content": "That's great! Please generate another one."},
	        {"role": "assistant", "content": "Find a live feed of a cute zoo animal and store a snapshot image of the animal in the local directory."},
            {"role": "user", "content": "That's great! Please generate another one."}],
        temperature=0.7
    )
    # Extract the generated script from the API response
    response = response['choices'][0]['message']['content']
    return response

# Use OpenAI.ChatCompletion.create to generate a short name to title the subdirectory for user input and output.
def generate_name(input):
	prompt = f"Please come up with a short name to title the subdirectory for the following prompt:\n{input}"
	name = openai.ChatCompletion.create(
		model=model,
		messages=[
			{"role": "system", "content": "You are a name generating assistant that takes a user input and generates a short name to describe the task. Output should be formatted with underscores. For example, 'find_the_current_weather_in_philadelphia'."},
			{"role": "user", "content": "Get monthly unemployment rate data in the U.S. from https://data.bls.gov/timeseries/LNS14000000. Parse the table and print the data for 2022 in the terminal."},
			{"role": "assistant", "content": "us_unemployment_rate_2022"},
			{"role": "user", "content": prompt}],
		max_tokens=3000,
		n=1,
		stop=None,
		temperature=0.7
	)
	# Extract the generated script from the API response
	name = name['choices'][0]['message']['content']
	return name

suggestions_boilerplate = "Make suggestions and recommendations, written out in detail. List steps to take, but don't write out full code. You can use pseudocode. Avoid 'example' URLs. Only use API keys if the user has given them to you in the prompt. If an API key is not part of the prompt, DO NOT REQUIRE API KEYS IN YOUR CODE. If you encounter any of these problems, change your approach. We want to make the code do what the user wants right out of the box! Assume no libraries have been installed previously. If you need any libraries, write a function to install them in the local environment."

def generate_pseudo_code(input):
	prompt = f"How would you write a Python script that does the following:\n{input}\n{suggestions_boilerplate}"
	pseudo_code = generate_suggestions(prompt)
	return pseudo_code

def generate_error_suggestions(input, prev_response, tests, test_results):
	prompt = f"You previously produced a faulty response to the following prompt: 'Write Python code that solves the following prompt:\n{input}\nThe most recent faulty response was:\n'''\n{prev_response}\n'''\nWe ran the following tests (stored at '/temp/temp_tests.py'):\n{tests}\nThe faulty response failed the tests as such:\n'''{test_results}'''\nHow would you fix this error while also ensuring you meet user needs? {suggestions_boilerplate}"
	error_suggestions = generate_suggestions(prompt)
	return error_suggestions