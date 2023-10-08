from . import init_functions as functions

def init_command(args):
    # create folders
    folders = functions.create_folders(args)
    if folders != 'ok':
        print('CREATING FOLDERS: ' + folders)
        exit()
    print('CREATING FOLDERS: ' + folders)

    # create files
    files = functions.create_files(args)
    if files != 'ok':
        print('CREATING FILES: ' + files)
        exit()
    print('CREATING FILES: ' + files)

    # create docker files
    if args.docker:
        dockerfile = functions.create_dockerfile(args)
        if dockerfile != 'ok':
            print('CREATING DOCKER FILES: ' + dockerfile)
            exit()
        print('CREATING DOCKER FILES: ' + dockerfile)

    # install dependencies
    if args.requirements:
        requirements = functions.install_dependencies(args)
        if requirements != 'ok':
            print('INSTALLING REQUIREMENTS:' + requirements)
            exit()
        print('INSTALLING REQUIREMENTS:' + requirements)

    # create server file
    if args.server:
        server = functions.create_server(args)
        if server != 'ok':
            print('CREATING SERVER FILE:' + server)
            exit()
        print('CREATING SERVER FILE:' + server)

    # create github actions related folder and files
    if args.actions:
        github_actions = functions.create_actions(args)
        if github_actions != 'ok':
            print('CREATING GITHUB ACTIONS: ' + github_actions)
            exit()
        print('CREATING GITHUB ACTIONS: ' + github_actions)

