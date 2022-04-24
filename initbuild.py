import getpass
import pathlib
import sys
import getopt

def configauth():
    sender = input("Dedicated sender email address: ")
    recip = input("Recipient email address (leave blank if same as Sender): ") or sender
    passw = getpass.getpass(prompt='Password for Sender email address: ')

    with open(str(pathlib.Path.home()) + "/.loglistenerproject.env", "a") as f:
        f.write("SENDER=%s\n" % (sender))
        f.write("RECIPIENT=%s\n" % (recip))
        f.write("PASSW=%s\n" % (passw))

def get_options(argvs):
    try:
        opts, args = getopt.getopt(argvs, "ib", ["build"])
    except getopt.GetoptError:
        print("please try python3 initauth.py -i <info>", file=sys.stderr)
        exit(1)

    for opt, arg in opts:
        if opt == '-i':
            print("python3 authinit.py -i <info> -b <build>")
        elif opt in ['-b', '--build']:
            configauth()

def run():
    argvs = sys.argv[1:]
    get_options(argvs)

if __name__ == '__main__':
    exit(run())
