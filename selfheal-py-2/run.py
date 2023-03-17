# Function that runs code and returns exceptions
def run(code):
    # Run the code
    try:
        exec(code)
    except Exception as e:
        return e
    else:
        return None