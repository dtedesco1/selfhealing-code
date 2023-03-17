import openai

# Set the OpenAI API key
openai.api_key = open("../key.txt", "r").read().strip("\n")

model = "gpt-4"