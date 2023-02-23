#Import libraries and set variables
import smtplib
import ssl
import os
from email.message import EmailMessage

#User's email, google generated password, and recipients
#Note, the password is NOT the user's password but is instead generated through google's app password which can be found in the settings

email_sender = 'insert personal username'
email_password = 'google authentication password'
email_receiver = 'email recipient(s)'

#Email contents
subject = 'Subject'
body = """
Insert the message that you want to send here!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#Layer of security
context = ssl.create_default_context()

#Log in and send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())