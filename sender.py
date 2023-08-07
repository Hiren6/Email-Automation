import os
from dotenv import load_dotenv
import pandas as pd
import smtplib
from email.message import EmailMessage
from email.utils import formataddr

load_dotenv()

email_sender = os.getenv('EMAIL_SENDER')
email_password = os.getenv('EMAIL_PASSWORD')

subject = 'Invitation for Proteomics Workshop Independence-Day'

df = pd.read_csv('email_data.csv')

total_emails_sent = 0

for _, row in df.iterrows():
    receiver_name = row['Name']
    receiver_email = row['Email Address']
    msg = EmailMessage()
    msg['From'] = formataddr(('SWASTOME', f'{email_sender}'))
    msg['To'] = receiver_email
    msg['Subject'] = subject
    body = f'''\
        Dear {receiver_name}, \n
        We are happy to register you for the Virtual Hands on Session.
        We look forward to seeing you there! :)\n
        Regards,
        Swastome
    '''
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, receiver_email, msg.as_string())
        print(f'Email sent to {receiver_email}')
        total_emails_sent += 1

print(f'Sent a total of {total_emails_sent} emails!')