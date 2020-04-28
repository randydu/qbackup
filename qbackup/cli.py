import sys

def main(*argv):
    # loads all plugin tasks under the "./tasks" folder
    from . import tasks

    print("CLI >>", *argv)

    from . import cmd
    cmd.run()



if __name__ == "__main__": 
    sys.exit(main(sys.argv))