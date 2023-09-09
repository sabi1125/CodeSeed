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

args = parser.parse_args()

# create folders
create_folders = util.create_folders(args)
if create_folders != 'ok':
    exit()
print(create_folders)

# create files
create_files = util.create_files(args)
if create_files != 'ok':
    exit()
print(create_files)

# create docker files
if args.docker:
    create_dockerfile = util.create_dockerfile(args)
    if create_dockerfile != 'ok':
        exit()
    print(create_dockerfile)

# create server file
if args.server:
    create_server = util.create_server(args)
    if create_server != 'ok':
        exit()
    print(create_server)
