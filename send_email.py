import smtplib

sender = "bjlslopez@gmail.com"
receiver = "bjlslopez@gmail.com"
password = ""
subject = "Python email test"
body = "I wrote an email! :D"

# header
message = f"""From: Bayardo Lopez{sender}
To: Pablo Lopez{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")