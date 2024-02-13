import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to the user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function to interact with the user
def main():
    speak("Hello! I am your Python voice assistant. How can I help you today?")
    
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hi there!")
        elif "how are you" in query:
            speak("I'm doing well, thank you for asking!")
        elif "what is your name" in query:
            speak("I am a Python voice assistant.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()