import sys
import getopt
import pathlib
import initbuild

def get_path(opts):
    path = str(pathlib.Path.home())
    for opt, arg in opts:
        if opt in ['-p', '--path']:
            path = arg
            break
    return path
 
def get_options(opts):
    for opt, arg in opts:
        if opt in ['-i', '--info']:
            print("python3 initbuild.py -i <info> -p <path> -b <build>")
            return 0
        elif opt in ['-b', '--build']:
            initbuild.configauth(path=get_path(opts))

def run():
    argvs = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argvs, "ibp:", ["info", "build", "path="])
    except getopt.GetoptError:
        print("please try python3 initauth.py -i <info>", file=sys.stderr)
        exit(1)

    get_options(opts)

if __name__ == '__main__':
    exit(run())
