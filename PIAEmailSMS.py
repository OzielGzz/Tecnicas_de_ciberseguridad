import email, smtplib, ssl
import os.path
import getpass
import argparse
import configparser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client

def send_emailP(e,co,re,a,b,f):
    sender_email = e
    password = co
    receiver_email = re
    subject = a
    body = b
    if f != 'no':
        file_location = f
    else:
        pass

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  

    message.attach(MIMEText(body, "plain"))

    if f != 'no':
        filename = os.path.basename(file_location) 

        with open(file_location, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
          
        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(part)
    else:
        pass
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

def send_smsP(SID,to,n,d,m):
    accountSID = SID
    authToken = to

    twilioCli = Client(accountSID,authToken)

    myTwilioNumber = n

    destCellPhone = d

    msg = m
    message = twilioCli.messages.create(to = destCellPhone,
                                        from_ = myTwilioNumber,
                                        body = msg)
    print(message.to)
    print(message.from_)
    print(message.body)

    print(message.sid)
    print(message)
    print(type(message))
    print(message.status)
    print(message.date_created)
    print(message.date_sent)

