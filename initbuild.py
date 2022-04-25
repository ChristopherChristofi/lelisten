import getpass

def configauth(path=None):
    sender = input("Dedicated sender email address: ")
    recip = input("Recipient email address (leave blank if same as Sender): ") or sender
    passw = getpass.getpass(prompt='Password for Sender email address: ')

    with open(str(path) + "/.loglistenerproject.env", "a") as f:
        f.write("SENDER=%s\n" % (sender))
        f.write("RECIPIENT=%s\n" % (recip))
        f.write("PASSW=%s\n" % (passw))
    return 0
