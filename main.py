from command_parser import parse_and_execute, set_base_path

def main():
    print("🧠 AI Assistant (type 'exit' to quit)")
    set_base_path()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = parse_and_execute(user_input)
        print(f"🤖: {result}")

if __name__ == "__main__":
    main()
