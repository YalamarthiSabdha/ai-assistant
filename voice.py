import pyttsx3
import os

# Try importing speech recognition only if it's available (i.e., local)
try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False

def speak(text):
    """Speak the given text aloud."""
    print(f"🤖 Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def listen(timeout=5, phrase_time_limit=10):
    """Listen to the user's voice and return the recognized command as text."""
    if not SR_AVAILABLE:
        return "Voice input not supported in this environment."

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        with mic as source:
            print("🎙️ Listening... (Speak now)")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    except sr.WaitTimeoutError:
        return "Listening timed out, no speech detected."

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command
    except sr.UnknownValueError:
        return "Sorry, I could not understand what you said."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
