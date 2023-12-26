from . import init_functions as functions

def init_command(args):
    # create folders
    folders = functions.create_folders(args)
    if folders != 'DONE':
        print('CREATING FOLDERS: ' + folders)
        return
    print('CREATING FOLDERS: ' + folders)

    # create files
    files = functions.create_files(args)
    if files != 'DONE':
        print('CREATING FILES: ' + files)
        return
    print('CREATING FILES: ' + files)

    # create docker files
    if args.docker:
        dockerfile = functions.create_dockerfile(args)
        if dockerfile != 'DONE':
            print('CREATING DOCKER FILES: ' + dockerfile)
            return
        print('CREATING DOCKER FILES: ' + dockerfile)

    # install dependencies
    if args.requirements:
        requirements = functions.install_dependencies(args)
        if requirements != 'DONE':
            print('INSTALLING REQUIREMENTS:' + requirements)
            return
        print('INSTALLING REQUIREMENTS:' + requirements)

    # create server file
    if args.server:
        server = functions.create_server(args)
        if server != 'DONE':
            print('CREATING SERVER FILE:' + server)
            return
        print('CREATING SERVER FILE:' + server)

    # create github actions related folder and files
    if args.actions:
        github_actions = functions.create_actions(args)
        if github_actions != 'DONE':
            print('CREATING GITHUB ACTIONS: ' + github_actions)
            return
        print('CREATING GITHUB ACTIONS: ' + github_actions)

    # add remote repository
    if args.url:
        add_remote = functions.add_remote_repository(args)
        if add_remote != 'DONE':
            print('ADDING REMOTE REPOSITORY: ' + add_remote)
            return
        print('ADDED REMOTE REPOSITORY: ' + add_remote)

    create_dotfiles = functions.create_dotfiles(args)
    print('CREATING DOTFILE: ' + create_dotfiles)

