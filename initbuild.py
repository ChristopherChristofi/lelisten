import getpass

def configauth(path=None):
    sender = input("Dedicated sender email address: ")
    recip = input("Recipient email address (leave blank if same as Sender): ") or sender
    passw = getpass.getpass(prompt='Password for Sender email address: ')
    msg = input("Message (leave blank for default): ") or "Loglistener says Hello."
    subj = input("Subject Line (leave blank for default): ") or "Log Message" 

    with open(str(path), "+w") as f:
        f.write("SENDER=%s\n" % (sender))
        f.write("RECIPIENT=%s\n" % (recip))
        f.write("PASSW=%s\n" % (passw))
        f.write("MESSAGE=%s\n" % (msg))
        f.write("SUBJECT=%s\n" % (subj))
    return 0
