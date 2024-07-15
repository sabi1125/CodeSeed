import argparse
import platform
import os

from commands.init import init
from commands.create import create

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")
# version
version = parser.add_argument("-v","--version", action="version", version="CodeSeed v0.2.1" ,help="DISPAYS CURRENT INSTALLED CODESEED VERSION")

# init command
init_parser = subparser.add_parser("init", help="INITILIZES INIT COMMAND")
init_parser.add_argument("foldername", help="ADD THE FOLDERNAME")
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

init_parser.add_argument('--ignore-config', 
                         nargs='+',
                         dest='ignoreconfig',
                         default='',
                         choices=['docker', 'git'],
                         help='SPECIFY THE IGNORE FILES YOU DONOT WANT TO CREATE')

# create command
create_parser = subparser.add_parser("create", help="CREATES CONTROLLER, INTERACTOR AND REPOSITORY FILES")
create_parser.add_argument("files", 
                           nargs='+',
                           help="ADD THE FILENAME OR MULTIPLE FILE NAMES")

create_parser.add_argument('--with-test',
                           action='store_true',
                           dest='withtest',
                           help='CREATE FILES WITH TEST FILES'
                           )


args = parser.parse_args()
args.platform = platform.system()

if args.command == "init":
    init.init_command(args)
elif args.command == "create":
    create.create_command(args)
elif args.command == "version":
    print(args)
