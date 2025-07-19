from command_parser import parse_and_execute, set_base_path
from voice import listen, speak

def text_mode():
    print("🧠 AI Assistant (type 'exit' to quit)")
    set_base_path()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = parse_and_execute(user_input)
        print(f"🤖: {result}")

def voice_mode():
    speak("Voice assistant started. You can now speak your command.")
    set_base_path()
    try:
        while True:
            command = listen()
            if command.lower() in ["exit", "quit", "stop"]:
                speak("Goodbye!")
                break
            response = parse_and_execute(command)
            speak(response)
    except KeyboardInterrupt:
        speak("Stopping the assistant. Goodbye!")

def main():
    print("👋 Welcome to your AI Assistant!")
    print("Choose mode:\n1. Text-based (type commands)\n2. Voice-based (speak commands)")
    mode = input("Enter 1 or 2: ").strip()
    if mode == "1":
        text_mode()
    elif mode == "2":
        voice_mode()
    else:
        print("Invalid choice. Please restart and enter 1 or 2.")

if __name__ == "__main__":
    main()
