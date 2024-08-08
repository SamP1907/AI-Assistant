import pyttsx3


# def list_voices():
#     engine = pyttsx3.init()
#     voices = engine.getProperty("voices")


def speak_from_text(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty("voice", voice.id)
            break
    rate = engine.getProperty("rate")
    engine.setProperty("rate", rate - 70)
    engine.say(text)
    engine.runAndWait()
