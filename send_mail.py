import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, recipient_email, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    smtp_user = "patilsampada580@gmail.com"
    smtp_password = "Pass@123.#"

    try:
        # Create a MIME object to represent the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        return "Email sent successfully."

    except smtplib.SMTPAuthenticationError:
        return "Authentication failed. Check your email and password."
    except smtplib.SMTPConnectError:
        return "Failed to connect to the server. Check your SMTP server and port."
    except Exception as e:
        return f"Failed to send email. Error: {e}"
