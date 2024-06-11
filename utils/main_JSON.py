import json

def json_minify(input_string):
    try:
        return json.dumps(json.loads(input_string), separators=(',', ':'))
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def json_beautify(input_string):
    try:
        return json.dumps(json.loads(input_string), indent=2)
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {e}"

def process_json():
    user_input = ""
    while True:
        line = input().strip()
        if not line:
            break
        user_input += line + "\n"

    if not user_input.strip():
        return

    action = input("Do you want to minify or beautify the JSON? (minify/beautify):\n").strip().lower()

    if action == "minify":
        result = json_minify(user_input)
    elif action == "beautify":
        result = json_beautify(user_input)
    else:
        result = "Invalid action. Please enter 'minify' or 'beautify'."

    print(result)

if __name__ == "__main__":
    process_json()


