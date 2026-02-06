import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import datetime
import wikipedia

# Initialize Voice
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust for ambient noise for better accuracy
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("...listening for command...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except:
        return "None"

def run_assistant():
    """Main logic for tasks"""
    speak("I am listening. What can I do for you?")
    query = take_command()

    if 'edureka' in query:
        speak("Opening Edureka. What is your query?")
        search = take_command()
        wb.open(f"https://www.edureka.co/search/{search}")
    
    elif 'video' in query:
        speak("What should I look up on YouTube?")
        search = take_command()
        wb.open(f"https://www.youtube.com/results?search_query={search}")

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        results = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
        speak(results)

    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"It is currently {time}")

    elif 'go to sleep' in query:
        speak("Standing by. Just say my name if you need me.")
        return False # This exits the active loop
    
    return True

if __name__ == "__main__":
    WAKE_WORD = "nova"
    print(f"Assistant is IDLE. Say '{WAKE_WORD}' to wake me up.")
    
    while True:
        # Step 1: Passive Listening
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        
        try:
            # Check if the wake word was in the snippet of audio
            voice_input = r.recognize_google(audio).lower()
            
            if WAKE_WORD in voice_input:
                # Step 2: Switch to Active Mode
                active = True
                while active:
                    active = run_assistant()
                    
        except Exception:
            # If it doesn't recognize anything, it just loops back to listening
            continue