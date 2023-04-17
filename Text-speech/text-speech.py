import pyttsx3

# Initialize the Text-to-Speech (TTS) engine
engine = pyttsx3.init()

# Set the rate of speech
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate

# Set the voice
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

# Read the text file
with open('text.txt', 'r') as file:
    text = file.read().replace('\n', '')

# Convert text to speech
engine.say(text)
engine.runAndWait()
