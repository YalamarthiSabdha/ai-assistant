from command_parser import parse_and_execute, set_base_path
from voice import listen, speak

def main():
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

if __name__ == "__main__":
    main()
