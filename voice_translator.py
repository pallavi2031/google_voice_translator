
# print(googletrans.LANGUAGES) 

import googletrans
import speech_recognition as sr
import gtts
import playsound

# Set the source and destination languages
srclang = "hi"  # Source language (e.g., Hindi)
dest = "fr"    # Destination language (e.g., French)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Use a microphone as the audio source
with sr.Microphone() as source:
    print("Speak now")
    voice = recognizer.listen(source)  # Listen for audio input
    text = recognizer.recognize_google(voice, language=srclang)  # Perform speech recognition
    print(text)

# Translate the recognized text to the destination language
translator = googletrans.Translator()
translation = translator.translate(text, dest=dest)
print(translation.text)

# Convert the translated text to audio
converted_audio = gtts.gTTS(translation.text, lang=srclang)
converted_audio.save("hello.mp3")  # Save the audio as an MP3 file

# Play the translated audio
playsound.playsound("hello.mp3")
