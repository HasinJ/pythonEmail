import smtplib, ssl, getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "hasin.choudhury@cplusmanagement.com"  # Enter your address
receiver_email = "it@cplusmanagement.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = f"""\
Subject: Error in Application

Application has thrown an error. Please check logs for "date".

DO NOT REPLY."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
