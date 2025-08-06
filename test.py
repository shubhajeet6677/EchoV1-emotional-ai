import speech_recognition as sr
import pyaudio
import os
import pyttsx3
import webbrowser
import subprocess

def say(text):
    """Function to convert text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def InputCMD():
    """Function to listen for audio input and convert it to text."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio , language="en-US")
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None


if __name__ == "__main__":
    say("Hello, how can I help you today?")

    print("Listening for command...")

    command = InputCMD()
    say(command if command else "I didn't catch that.")

    sites = [["YouTube", "https://www.youtube.com"],
             ["google", "https://www.google.com"],
             ["wikipedia", "https://www.wikipedia.org"],
             ["github", "https://github.com/mlwithharsh"],
             ["stackoverflow", "https://stackoverflow.com"]]
    for site in sites:
        if f"open {site[0].lower()}" in command.lower():
            say(f"Opening {site[0]}")
            webbrowser.open(site[1])
        
    if "open college memories" in command.lower():
        say("Opening college memories")
        # subprocess.Popen(['start', 'C:\\Users\\Harsh Sharma\\OneDrive\\COLLEGE MEMORIES'], shell=True)
        os.startfile(r"C:\Users\Harsh Sharma\OneDrive\COLLEGE MEMORIES")
# webdriver to login to a website
