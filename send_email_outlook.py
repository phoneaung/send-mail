from email.message import EmailMessage
from decouple import config

import smtplib

print('Hello stranger! Who do you want to email today?')

# prompt user input
email_sender = 'phone.aung@outlook.com'
# paste the app password generated from email service
email_password = config('OUTLOOK_PASSWORD')

email_receiver = input("Enter receipient's email address: ")
subject = input("Subject: ")
body = input("Body: ")

email = EmailMessage()

email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject

# Specify UTF-8 encoding for the email body
email.set_content(body)

# Use a try-except block to handle potential exceptions
try:
    # create SSL context
    # specifying the CA certificate bundle using certifi 
    # context = ssl.create_default_context(cafile=certifi.where())

    # disable certificate verification 
    # context.check_hostname = False
    # context.verify_mode = ssl.CERT_NONE

    with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
        # start tls
        smtp.starttls()

        # Login to the SMTP server
        smtp.login(email_sender, email_password)

        # Send email
        smtp.sendmail(email_sender, email_receiver, email.as_string())
        print('Email sent successfully!')

except Exception as error:
    print(f'An error has occurred: {str(error)}')


