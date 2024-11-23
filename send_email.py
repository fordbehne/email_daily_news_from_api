import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ford01286@gmail.com"
    password = "jieo oqsw mnxe scmc"
    # password = os.getenv("PASSWORD")
    # This is how to hide the password but you also need to
    # go to environmental variables in the computer
    # if help is needed go to video 222 in Python Mega Course training to refresh

    receiver = "ford01286@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
