import sys
import os
import getopt
import pathlib
import initbuild
import test_send

def get_path(opts=None):
    path = str(pathlib.Path.home())
    for opt, arg in opts:
        if opt in ['-p', '--path']:
            path = arg
            break
    return path + "/.loglistenerproject.env"
 
def get_options(opts, path):
    for opt, arg in opts:
        if opt in ['-i', '--info']:
            print("python3 initbuild.py -i <info> -p <path> -b <build>")
            return 0
        elif opt in ['-b', '--build']:
            initbuild.configauth(path=path)
        # dev only option
        elif opt in ['-r', '--run']:
            # only works if path set
            test_send.serve_mail(path)

def run():
    argvs = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argvs, "ibrp:", ["info", "build", "run", "path="])
    except getopt.GetoptError:
        print("please try python3 initauth.py -i <info>", file=sys.stderr)
        exit(1)

    path = get_path(opts)

    get_options(opts, path)

if __name__ == '__main__':
    exit(run())
