import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# dev dependencies
import dotenv
import pathlib

def read_climate():
    # TODO to be based on env file not dotenv lib
    sender = os.getenv('SENDER')
    recipient = os.getenv('RECIPIENT')
    password = os.getenv('PASSW')
    subject = os.getenv('SUBJECT')
    message = os.getenv('MESSAGE')
    return sender, recipient, password, subject, message

def email_meta():
    
    sender_email, recipient_email, passw, subj, msg = read_climate()
    
    email_meta = {
        'sender': sender_email,
        'target': recipient_email,
        'passw': passw,
        'message': msg,
        'subject': subj
    }
    return email_meta

def start_serve():

    msg = MIMEMultipart()

    struct_email = email_meta()
    password = struct_email.get('passw')
    msg['From'] = struct_email.get('sender')
    msg['To'] = struct_email.get('target')
    msg['Subject'] = struct_email.get('subject')
    msg.attach(MIMEText(struct_email.get('message'), 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(['From'], msg['To'], msg.as_string())

    server.quit()

    print("email should have been sent to: %s" % (struct_email.get('target')))

def serve_mail(path):
    # dev
    dotenv.load_dotenv(dotenv_path=pathlib.Path(path))
    start_serve()
    return 0

if __name__ == '__main__':
    # TODO path dependency only required in current dev
    exit(serve_mail(path))
