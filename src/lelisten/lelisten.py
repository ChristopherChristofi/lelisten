import sys, os, getopt, pathlib
from src.utils import build_env, test_email_service

info_help_notes = ( "Info:   -i, --info      call for help information\n"
                    "Build:  -b, --build     set to build .env variables for email service in /<home>/.lelisten.env\n"
                    "Path:   -p, --path      set path for .env variables for email service, rather than default home, i.e /<home>/make/new/path\n"
                    "Run:    -r, --run       initiate email send message service.\n")

def get_path(opts=None):
    path = str(pathlib.Path.home())
    for opt, arg in opts:
        if opt in ['-p', '--path']:
            path = arg
            break
    return path + "/.lelisten.env"
 
def get_options(opts, path):
    for opt, arg in opts:
        if opt in ['-i', '--info']:
            print(info_help_notes)
            return 0
        elif opt in ['-b', '--build']:
            build_env.configauth(path=path)
            return 0
        # dev only option OR to become test implement
        elif opt in ['-r', '--run']:
            # only works if path set
            test_email_service.serve_mail(path)

def run():
    argvs = sys.argv[1:]
    # does not catch err non-specified options, such as: lelisten error (only -e/--error)
    try:
        opts, args = getopt.getopt(argvs, "ibrp:", ["info", "build", "run", "path="])
    except getopt.GetoptError:
        print("please try 'lelisten -i <info>'", file=sys.stderr)
        exit(1)

    if not argvs: # no options provided - possible to remove when .env manual creation-read added
        print("please try 'lelisten -i <info>'", file=sys.stderr)
        exit(1)

    path = get_path(opts)

    get_options(opts, path)

if __name__ == '__main__':
    exit(run())
