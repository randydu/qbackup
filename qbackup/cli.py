import sys

def main(*argv):
    print("CLI >>", *argv)


if __name__ == "__main__": 
    sys.exit(main(sys.argv))