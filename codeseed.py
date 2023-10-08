import argparse
from commands.init import init

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")

init_parser = subparser.add_parser("init", help="initilizes init command")
init_parser.add_argument("filename", help="add the filename")
init_parser.add_argument('-l', '--lang', 
                    dest='language',
                    choices=['golang','typescript'],
                    default='typescript',
                    help='SPECIFY THE LANGUAGE YOU WANT YOUR PROJECT TO BE IN')

init_parser.add_argument('-d', '--docker', 
                    action='store_true',
                    dest='docker',
                    help='SPECIFY IF YOU WANT YOUR PROJECT TO HAVE DOCKER FILES')

init_parser.add_argument('-r', '--requirements', 
                    action='store_true',
                    dest='requirements',
                    help='REQUIREMENTS INSTALLS THE PACKAGES(DEPENDENCIES) THAT IS REQUIRED FOR THE PROJECT')

init_parser.add_argument('-s', '--server',
                    action='store_true',
                    dest='server',
                    help='SPECIFY IF YOU WANT A BASIC SERVER FILE TO BE ADDED')

init_parser.add_argument('-a', '--actions',
                    action='store_true',
                    dest='actions',
                    help='SPECIFY IF YOU WANT A GITHUB ACTIONS TO BE ADDED')

init_parser.add_argument('-u', '--url',
                        dest='url',
                        help='ADD URL TO THE REMOTE REPOSITORY')

args = parser.parse_args()

if args.command == "init":
    init.init_command(args)
