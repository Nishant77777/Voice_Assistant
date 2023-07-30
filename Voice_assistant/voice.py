import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Error making the request to Google Speech Recognition API: {e}")
        return None

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you?")
    while True:
        user_input = listen()
        if user_input:
            
            if "hello" in user_input.lower():
                speak("Hello!")
            elif "what's your name" in user_input.lower():
                speak("My name is Nothing.")
            elif "exit" in user_input.lower():
                speak("sayonara!")
                break
            else:
                speak("I didn't catch that. Can you please repeat?")
