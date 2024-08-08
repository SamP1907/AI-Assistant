import tkinter as tk
from tkinter import messagebox

import send_mail


def show_email_gui():
    def send_email():
        sender_email = sender_entry.get()
        recipient_email = recipient_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END).strip()

        if sender_email and recipient_email and subject and body:
            result = send_mail.send_email(sender_email, recipient_email, subject, body)
            messagebox.showinfo("Email Status", result)
        else:
            messagebox.showwarning("Input Error", "All fields must be filled out.")

    # Create the main window
    root = tk.Tk()
    root.title("Send Email")
    root.geometry("400x500")  # Fixed size
    root.resizable(False, False)  # Prevent resizing

    # Customize window background color
    root.configure(bg="#f5f5f5")  # Light grey background

    # Title Label
    title_label = tk.Label(
        root, text="Send Email", font=("Arial", 16, "bold"), bg="#f5f5f5", pady=10
    )
    title_label.pack()

    # Sender Email
    sender_label = tk.Label(
        root, text="Sender Email:", bg="#f5f5f5", font=("Arial", 12)
    )
    sender_label.pack(pady=(10, 0))
    sender_entry = tk.Entry(root, width=50, font=("Arial", 12))
    sender_entry.pack(pady=(0, 10))

    # Recipient Email
    recipient_label = tk.Label(
        root, text="Recipient Email:", bg="#f5f5f5", font=("Arial", 12)
    )
    recipient_label.pack(pady=(0, 0))
    recipient_entry = tk.Entry(root, width=50, font=("Arial", 12))
    recipient_entry.pack(pady=(0, 10))

    # Subject
    subject_label = tk.Label(root, text="Subject:", bg="#f5f5f5", font=("Arial", 12))
    subject_label.pack(pady=(0, 0))
    subject_entry = tk.Entry(root, width=50, font=("Arial", 12))
    subject_entry.pack(pady=(0, 10))

    # Body
    body_label = tk.Label(root, text="Body:", bg="#f5f5f5", font=("Arial", 12))
    body_label.pack(pady=(0, 0))
    body_text = tk.Text(
        root,
        width=50,
        height=10,
        wrap=tk.WORD,
        bg="#e0f7fa",
        font=("Arial", 12),
        borderwidth=2,
        relief="groove",
    )
    body_text.pack(pady=(0, 10))

    # Add placeholder text to the Text area
    body_text.insert(tk.END, "Write your email body here...")

    # Send Button
    send_button = tk.Button(
        root,
        text="Send",
        command=send_email,
        bg="#0047AB",
        fg="white",
        font=("Arial", 12, "bold"),
    )
    send_button.pack(pady=(10, 5))

    # Cancel Button
    cancel_button = tk.Button(
        root,
        text="Cancel",
        command=root.destroy,
        bg="#0033A0",
        fg="white",
        font=("Arial", 12, "bold"),
    )
    cancel_button.pack(pady=(5, 10))

    # Run the GUI event loop
    root.mainloop()
