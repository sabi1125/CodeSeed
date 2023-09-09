import argparse

parser = argparse.ArgumentParser()

parser.add_argument('create', 
                    help="CREATES FOLDER'S AND FILES FOR YOUR PROJECT")

parser.add_argument('-l', '--lang', 
                    dest='language',
                    choices=['go','ts'],
                    default='ts',
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


