import sys, os, getopt, pathlib
from src.utils import test_email_service

info_help_notes = ( "Info:   -i, --info      call for help information\n"
                    "Build:  -b, --build     set to build .env variables in /<home>/.lelisten/.lelisten.env\n"
                    "Run:    -r, --run       initiate email send message service.\n")

env_build = {}

def get_env_variables_user_input():
    env_build['sender'] = input("Dedicated sender email address: ")
    if env_build['sender'] == '':
        print("Please provide a valid email address, dedicated sender cannot be left blank", file=sys.stderr)
        exit(1)
    env_build['recipient'] = input("Recipient email address (leave blank if same as Sender): ") or env_build['sender']
    env_build['message'] = input("Message (leave blank for default): ") or "Loglistener says Hello."
    env_build['subject'] = input("Subject Line (leave blank for default): ") or "Log Message"
    env_build['api_client_auth'] = input("File name for Google API client secret (leave blank for default): ") or "google_client_secret.json"
    return 0

def get_env_path(build=0, selected_file=".lelisten.env"):
    path_env_folder = str(pathlib.Path.home()) + "/.lelisten"
    if not os.path.exists(path_env_folder) and build == 1:
        os.makedirs(path_env_folder)
    return path_env_folder + "/" + selected_file

def config_env_file(path=None):
    with open(str(path), "+w") as f:
        f.write("SENDER=%s\n" % (env_build['sender']))
        f.write("RECIPIENT=%s\n" % (env_build['recipient']))
        f.write("MESSAGE=%s\n" % (env_build['message']))
        f.write("SUBJECT=%s\n" % (env_build['subject']))
        f.write("CLIENT_SECRETS=%s\n" % (get_env_path(selected_file=env_build['api_client_auth'])))
    return 0

def get_options(opts):
    for opt, arg in opts:
        if opt in ['-i', '--info']:
            print(info_help_notes)
            return 0
        elif opt in ['-b', '--build']:
            # get valid email address input before
            # .lelisten/ built.
            get_env_variables_user_input()
            path = get_env_path(build=1)
            config_env_file(path=path)
            return 0
        # dev only option OR to become test implement
        elif opt in ['-r', '--run']:
            # TODO validate .env variables
            path = get_env_path(build=0)
            test_email_service.serve_mail(path=path)

def run():
    argvs = sys.argv[1:]
    # does not catch err non-specified options, such as: lelisten error (only -e/--error)
    try:
        opts, args = getopt.getopt(argvs, "ibr", ["info", "build", "run"])
    except getopt.GetoptError:
        print("please try 'lelisten -i <info>'", file=sys.stderr)
        exit(1)

    if not argvs: # no options provided - possible to remove when .env manual creation-read added
        print("please try 'lelisten -i <info>'", file=sys.stderr)
        exit(1)

    get_options(opts)

if __name__ == '__main__':
    exit(run())
