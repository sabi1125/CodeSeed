from . import init_functions as functions

def init_command(args):
    # create folders
    folders = functions.create_folders(args)
    if folders != 'DONE':
        print('PROBLEM CREATING PROJECT FOLDERS')
        return
    print('CREATING FOLDERS: ' + folders)

    # create files
    files = functions.create_files(args)
    if files != 'DONE':
        print('PROBLEM CREATING PROJECT FILES')
        return
    print('CREATING FILES: ' + files)

    # create docker files
    if args.docker:
        dockerfile = functions.create_dockerfile(args)
        if dockerfile != 'DONE':
            print('PROBLEM CREATING DOCKERFILES')
            return
        print('CREATING DOCKER FILES: ' + dockerfile)

    # install dependencies
    if args.requirements:
        requirements = functions.install_dependencies(args)
        if requirements != 'DONE':
            print('PROBLEM INSTALLING DEPENDENCIES')
            return
        print('INSTALLING REQUIREMENTS:' + requirements)

    # create server file
    if args.server:
        server = functions.create_server(args)
        if server != 'DONE':
            print('PROBLEM CREATING SERVER FILES')
            return
        print('CREATING SERVER FILE:' + server)

    # create github actions related folder and files
    if args.actions:
        github_actions = functions.create_actions(args)
        if github_actions != 'DONE':
            print('PROBLEM CREATING GITHUB ACTIONS')
            return
        print('CREATING GITHUB ACTIONS: ' + github_actions)

    # add remote repository
    if args.url:
        add_remote = functions.add_remote_repository(args)
        if add_remote != 'DONE':
            print('PROBLEM ADDING REMOTE URL')
            return
        print('ADDED REMOTE REPOSITORY: ' + add_remote)

    create_dotfiles = functions.create_dotfiles(args)
    print('CREATING DOTFILE: ' + create_dotfiles)

