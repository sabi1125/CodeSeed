import argparse
from utils import util

parser = argparse.ArgumentParser()

parser.add_argument('project_dir', 
                    help="CREATES FOLDER'S AND FILES FOR YOUR PROJECT")

parser.add_argument('-l', '--lang', 
                    dest='language',
                    choices=['golang','typescript'],
                    default='typescript',
                    help='SPECIFY THE LANGUAGE YOU WANT YOUR PROJECT TO BE IN')

parser.add_argument('-d', '--docker', 
                    action='store_true',
                    dest='docker',
                    help='SPECIFY IF YOU WANT YOUR PROJECT TO HAVE DOCKER FILES')

parser.add_argument('-dp', '--dependencies', 
                    action='store_true',
                    dest='dependencies',
                    help='SPECIFY IF YOU WANT BASIC DEPENDENCIES TO BE INSTALLED')

parser.add_argument('-s', '--server',
                    action='store_true',
                    dest='server',
                    help='SPECIFY IF YOU WANT A BASIC SERVER FILE TO BE ADDED')

parser.add_argument('-a', '--actions',
                    action='store_true',
                    dest='actions',
                    help='SPECIFY IF YOU WANT A GITHUB ACTIONS TO BE ADDED')

args = parser.parse_args()

# create folders
create_folders = util.create_folders(args)
if create_folders != 'ok':
    print('CREATING FOLDERS: ' + create_folders)
    exit()
print('CREATING FOLDERS: ' + create_folders)

# create files
create_files = util.create_files(args)
if create_files != 'ok':
    print('CREATING FILES: ' + create_files)
    exit()
print('CREATING FILES: ' + create_files)

# create docker files
if args.docker:
    create_dockerfile = util.create_dockerfile(args)
    if create_dockerfile != 'ok':
        print('CREATING DOCKER FILES: ' + create_dockerfile)
        exit()
    print('CREATING DOCKER FILES: ' + create_dockerfile)

# install dependencies
if args.dependencies:
    install_dependencies = util.install_dependencies(args)
    if install_dependencies != 'ok':
        print('INSTALLING DEPENDENCIES:' + install_dependencies)
        exit()
    print('INSTALLING DEPENDENCIES:' + install_dependencies)

# create server file
if args.server:
    create_server = util.create_server(args)
    if create_server != 'ok':
        print('CREATING SERVER FILE:' + create_server)
        exit()
    print('CREATING SERVER FILE:' + create_server)

# create github actions related folder and files

if args.actions:
    create_actions = util.create_actions(args)
    if create_actions != 'ok':
        print('CREATING GITHUB ACTIONS: ' + create_actions)
        exit()
    print('CREATING GITHUB ACTIONS: ' + create_actions)

