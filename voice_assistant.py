import speech_recognition as sr
import pyttsx3
import pyautogui
from commands import execute_command

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user with a welcome message."""
    greeting = "Hello! I am your voice assistant. I am here to help you with typing and other tasks. Just speak your command."
    print(greeting)
    speak(greeting)

def listen():
    """Listen to the user's voice and return recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Service unavailable.")
    return ""

def process_command(command):
    """Process the voice command and type it or execute a basic action."""
    if execute_command(command):  # Checks if the command is a custom action
        return
    else:
        pyautogui.typewrite(command + '\n')  # Type out the command by default
