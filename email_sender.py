# This allows us to create and SMTP server. Whenever you email it needs to have a server that communicates the language of the email.
import smtplib
# smtp stands for simple mail transfer protocol.
from email.message import EmailMessage

# This template allows us to use the dollar sign $ to subsitute variables inside of texts within our HTML file
from string import Template

# this is similar to os.path. This allows us to access this index.html file
from pathlib import Path

# We wrap in template so it becomes a template object.
html = Template(Path('index.html').read_text())

email = EmailMessage()  # creates and email object.
email['from'] = 'Tyree Morris'  # Who is the email coming from? (Name)
email['to'] = 'motyre69@gmail.com'  # Where is the email going (email address)
# What is the subject of the email?
email['subject'] = 'You won a million dollars'

# Below formatting: 'html' tells the computer to parse it as html instead of complete html text document (won't show actual tags only content within body tags)
# The HTML document will contain the content of your email (the specific message you want to send)
email.set_content(html.substitute(name='TinTin'), 'html')

# In order to send, we have to use the smtp server to login to our client

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # tls is an ecryption mechanism that allows us to connect securely to the server
    smtp.starttls()
    # in order to send through G-mail, you will have to generate app password from gmail
    smtp.login('motyre69@gmail.com', 'jzqr qdfh vvge aflk ')
    smtp.send_message(email)
    print('all good boss!')  # confirmation that no errors exist
