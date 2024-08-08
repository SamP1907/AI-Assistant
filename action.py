import datetime
import os
import platform
import subprocess
import webbrowser

import pyjokes
import wikipediaapi

import email_gui
import text_to_speech
import weatherPrediction


# ACTION FUNCTION'S DEFINITIONS
def Action(send):
    user_data = send.lower()

    if "what is your name" in user_data:
        text_to_speech.speak_from_text("my name is Ziva. I'm your virtual assistant.")
        return "my name is Ziva.I'm your virtual assistant."

    # elif "hello" in user_data or "hay" in user_data or "hello Ziva":
    #     text_to_speech.speak_from_text("Hey sir, How i can  help you !")
    #     return "Hey sir, How i can  help you !"

    elif "how are you" in user_data:
        text_to_speech.speak_from_text("I am doing great these days sir")
        return "I am doing great these days sir"

    elif "thanku" in user_data or "thank" in user_data:
        text_to_speech.speak_from_text("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"

    elif "good morning" in user_data:
        text_to_speech.speak_from_text(
            "Good morning sir, i think you might need some help"
        )
        return "Good morning sir, i think you might need some help"

    elif "date today" in user_data or "current date" in user_data:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        text_to_speech.speak_from_text(f"Today's date is {current_date}")
        return f"Today's date is {current_date}"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + " Hour : ", (str)(
            current_time.minute
        ) + " Minute"
        text_to_speech.speak_from_text(Time)
        return str(Time)

    elif "shutdown" in user_data or "quit" in user_data:
        text_to_speech.speak_from_text("ok sir")
        return "ok sir"

    elif "open" in user_data and "website" in user_data:
        website = user_data.split("open ")[1].split(" website")[0].strip()
        webbrowser.open(f"https://{website}.com")
        text_to_speech.speak_from_text(f"{website} is now open")
        return f"{website} is now open"

    elif "weather" in user_data:
        ans = weatherPrediction.weather()
        text_to_speech.speak_from_text(ans)
        return ans

    elif "open calculator" in user_data or "calculator" in user_data:
        subprocess.Popen(["calc.exe"])
        response = "Calculator is now open."
        text_to_speech.speak_from_text(response)
        return response

    elif "music from my laptop" in user_data:
        url = "D:\\music"
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        text_to_speech.speak_from_text("songs playing...")
        return "songs playing..."

    elif "tell me a joke" in user_data or "tell a joke" in user_data:
        joke = pyjokes.get_joke()
        text_to_speech.speak_from_text(joke)
        return joke

    elif "search wikipedia" in user_data:
        user_data = user_data.replace("search wikipedia", "").strip()
        results = wikipediaapi.summary(user_data, sentences=2)
        text_to_speech.speak_from_text(results)
        return results

    elif "open notepad" in user_data:
        subprocess.Popen(["notepad.exe"])
        response = "Notepad is now open."
        text_to_speech.speak_from_text(response)
        return response

    elif "system information" in user_data or "system info" in user_data:
        system = platform.system()
        node = platform.node()
        release = platform.release()
        version = platform.version()
        machine = platform.machine()
        processor = platform.processor()

        response = (
            f"System Information:\n"
            f"Operating System: {system}\n"
            f"Computer Name: {node}\n"
            f"OS Release: {release}\n"
            f"OS Version: {version}\n"
            f"Machine Type: {machine}\n"
            f"Processor: {processor}"
        )

        text_to_speech.speak_from_text(response)
        return response

    elif "open file explorer" in user_data or "open files" in user_data:
        subprocess.Popen(["explorer.exe"])
        response = "File Explorer is now open."
        text_to_speech.speak_from_text(response)
        return response

    elif "send email" in user_data:
        email_gui.show_email_gui()  # Call the email GUI function
        return "Opening email interface."

    else:
        text_to_speech.speak_from_text("i'm able to understand!")
        return "i'm able to understand!"
