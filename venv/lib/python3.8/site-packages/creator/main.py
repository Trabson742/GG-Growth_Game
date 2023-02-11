import argparse
import os
import sys
from .copier import copy, get_script_path


def program(argv):
    parser = argparse.ArgumentParser(
        description="My flask  app boilerplate code"
    )
    parser.add_argument("appname", help="The application name")
    parser.add_argument("-d", "--destination", help="Folder to copy code to")
    args = parser.parse_args()
    script_dir = get_script_path(copy)
    appname = args.appname
    destination = args.destination
    if not destination:
        destination_path = os.path.join(os.getcwd(), appname)
    else:
        destination_path = os.path.join(destination, appname)
    return copy(script_dir, destination_path)


def main():
    program(sys.argv)


if __name__ == "__main__":
    main()
