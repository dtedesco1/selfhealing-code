import openai

# Set the OpenAI API key
openai.api_key = open("./key.txt", "r").read().strip("\n")

model = "gpt-4"
# model = "gpt-3.5-turbo"

general_prompt_boilerplate = f"\n- Make sure to avoid using 'example' URLs, URLs that do not provide the necessary data, or dummy API key or other configuration variables.\n- If an API key is not included in the user's original prompt, DO NOT ASK FOR OR REQUIRE API KEYS IN YOUR CODE. This is very important!\n- Do NOT EVER ask or expect the user to install external libraries. If any new external libraries are required, YOUR CODE MUST DO THE INSTALLATION. Use `pip3`.\n- Your code will be stored in the local directory as 'output.py' and tests will be stored at `tests.py`.\nIf you get stuck on any of the above issues, you might need to change your data source or avoid using an unavailable library or webpage. We want to make the code do what the user wants right out of the box!\nFinally, keep in mind that this is a loop--after you reply here, you will receive a copy of your code output, tests, and the test results and/or errors produced from this iteration. You'll be prompted in this way over multiple iterations, until you produce flawless code. You can leave hints for your later self, if that's helpful.\nI know you can do it--good luck!\n"