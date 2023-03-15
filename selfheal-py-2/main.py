import openai
import suggest_module
import code_module
import test_module

# Set the OpenAI API key
openai.api_key = open("./key.txt", "r").read().strip("\n")

def main():
    user_input = suggest_module.generate_inputs()
    print(user_input)
    pseudo_code_prompt = suggest_module.generate_pseudocode_prompt(user_input)
    pseudo_code = suggest_module.generate_suggestions(pseudo_code_prompt)
    print(pseudo_code)

    response_prompt = code_module.generate_code_prompt(user_input, pseudo_code)
    new_response = code_module.generate_code(response_prompt)
    print(new_response)

    tests_prompt = code_module.generate_tests_prompt(user_input, new_response)
    new_tests = code_module.generate_code(tests_prompt)
    print(new_tests)

    test_results = test_module.run_tests(new_tests)
    print(test_results)

if __name__ == "__main__":
    main()