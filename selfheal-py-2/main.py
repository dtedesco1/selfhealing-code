import openai
import suggest_module
import code_module

# Set the OpenAI API key
openai.api_key = open("./key.txt", "r").read().strip("\n")

def main():
    user_input = "Find the ages of David Beckham and Victoria Beckham, store the data in a DataFrame, and print the DataFrame to the console."
    pseudo_code_prompt = suggest_module.generate_pseudocode_prompt(user_input)
    pseudo_code = suggest_module.generate_suggestions(pseudo_code_prompt)
    print(pseudo_code)

    response_prompt = code_module.generate_code_prompt(user_input, pseudo_code)
    new_response = code_module.generate_code(response_prompt)
    print(new_response)

    test_prompt = code_module.generate_tests_prompt(user_input, new_response)
    new_test = code_module.generate_test(test_prompt)
    print(new_test)

    code_module.run_code(new_test)
    code_module.run_code(new_response)

if __name__ == "__main__":
    main()