import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "deucedhunter@gmail.com"
    password = os.environ.get("PASSWORD")

    receiver = "deucedhunter@gmail.com"
    context = ssl.create_default_context()

    print("Creating context to send email")
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print("Trying to login")
        server.login(username, password)
        print("Login successful")
        print("Sending email")
        server.sendmail(username, receiver, message.encode("utf8"))
        print("Email sent")