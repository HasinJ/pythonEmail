import smtplib, ssl, getpass

port = 465  # For SSL
password = getpass.getpass("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("hasin.choudhury@cplusmanagement.com", password)
    # TODO: Send email here
