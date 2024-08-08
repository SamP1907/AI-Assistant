from tkinter import *

from PIL import Image, ImageTk

import action
import speech_to_text

root = Tk()
root.title("You're Assistant")
root.geometry("750x750")
root.resizable(False, False)
root.config(bg="#7BB994")


# SEND function
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot != None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()


# ASK Function
def ask():
    ask_val = speech_to_text.recognize_speech_from_mic()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n")
    if bot_val != None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()


# DELETE Function
def delete():
    text.delete("1.0", "end")


# AI frameJ"_
# ?OL?]
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#7BB994")
frame.grid(row=0, column=1, padx=155, pady=10)

# text label
text_label = Label(
    frame, text="AI Assistant", font=("Helvetica", 12, "bold"), bg="#52916A"
)
text_label.grid(row=0, column=0, pady=20, padx=10)

# Image
image = ImageTk.PhotoImage(Image.open("../image/aiAssistant.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# adding Text widget
text = Text(root, font=("courir 10 bold"), bg="#52916A")
text.grid(row=2, column=0)

# Calculate the center coordinates
text_width = 375
text_height = 100
center_x = (750 - text_width) // 2
below_frame_y = 450
text.place(x=center_x, y=below_frame_y, width=text_width, height=text_height)

# entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=560, width=550, height=30)

# Define button width and height
button_width = 150
button_height = 60

# Calculate the positions of the buttons
total_button_width = button_width * 3
space_between_buttons = (750 - total_button_width) // 4

# button 1 (ASK)
button1 = Button(
    root,
    text="ASK",
    bg="#52916A",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=ask,
    width=button_width // 10,
    height=2,
)
button1.place(x=space_between_buttons, y=615)

# Button 2 (Send)
button2 = Button(
    root,
    text="Send",
    bg="#52916A",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=send,
    width=button_width // 10,
    height=2,
)
button2.place(x=2 * space_between_buttons + button_width, y=615)

# button 3 (Delete)
button3 = Button(
    root,
    text="Delete",
    bg="#52916A",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=delete,
    width=button_width // 10,
    height=2,
)
button3.place(x=3 * space_between_buttons + 2 * button_width, y=615)

root.mainloop()
