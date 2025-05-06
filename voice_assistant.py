import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the current time"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

def take_command():
    """Listen for user commands and return as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return "None"
    return command.lower()

def main():
    greet_user()
    while True:
        command = take_command()
        if 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'what time is it' in command or 'tell me the time' in command:
            time_str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_str}")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        else:
            speak("Please say the command again.")

if __name__ == "__main__":
    main()



