import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def do_report():
# Email Config
    sender_email = "lukacarter9@gmail.com"
    receiver_email = "simonkos1997@outlook.com" # client's email
    subject = "Daily Book Price Report"
    body = "Hello,\n\nPlease find attached today's book price report.\n\nBest,\nYour Automation Bot"
    password = "123123123!!"  # App Password, not your Gmail password!

    # Create the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Attach the Excel file
    filename = "data/cleaned_books.xlsx"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(filename)}",
        )
        message.attach(part)

    # Send Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)

    print("Email sent with Excel report attached!")