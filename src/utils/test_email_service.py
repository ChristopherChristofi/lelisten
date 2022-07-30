import os, base64
from src.utils import _gmail_api
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# dev dependencies
import dotenv
import pathlib

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

def read_env():
    # TODO to be based on env file not dotenv lib
    sender = os.getenv('SENDER')
    recipient = os.getenv('RECIPIENT')
    subject = os.getenv('SUBJECT')
    message = os.getenv('MESSAGE')
    return sender, recipient, subject, message

def email_meta():

    sender_email, recipient_email, subj, msg = read_env()

    email_meta = {
        'sender': sender_email,
        'target': recipient_email,
        'message': msg,
        'subject': subj
    }
    return email_meta

def start_send_service():

    service = _gmail_api.create_service(
            CLIENT_SECRET_FILE,
            API_NAME,
            API_VERSION,
            SCOPES
    )

    msg = MIMEMultipart()

    struct_email = email_meta()
    msg['To'] = struct_email.get('target')
    msg['Subject'] = struct_email.get('subject')
    msg.attach(MIMEText(struct_email.get('message'), 'plain'))
    raw_data_string = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    email_message = service.users().messages().send(userId=struct_email.get('sender'), body={'raw': raw_data_string}).execute()
    print("email should have been sent to: %s" % (struct_email.get('target')))

def serve_mail(path):
    print(path)
    # dev
    dotenv.load_dotenv(dotenv_path=pathlib.Path(path))
    start_send_service()
    return 0

if __name__ == '__main__':
    # TODO path dependency only required in current dev
    exit(serve_mail(path))
