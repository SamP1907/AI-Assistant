import speech_recognition as sr

import text_to_speech


def recognize_speech_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            voice_data = ""
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            text_to_speech.speak_from_text(
                "Sorry, I could not understand the audio. Please try again."
            )
        except sr.RequestError:
            text_to_speech.speak_from_text(
                "No internet connect. Please turn on internet connection"
            )
            return voice_data
