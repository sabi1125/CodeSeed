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

    # create config boilerplate (golang only, --initial-setup only) — the
    # config-aware logger/database variants below depend on the types
    # defined here
    if args.language == 'golang' and getattr(args, 'initial_setup', False):
        config = functions.create_config(args)
        if config != 'DONE':
            print('PROBLEM CREATING CONFIG FILE')
            return
        print('CREATING CONFIG FILE: ' + config)

    # create database connection boilerplate (golang only — same setup every project)
    if args.language == 'golang':
        database = functions.create_database(args)
        if database != 'DONE':
            print('PROBLEM CREATING DATABASE FILE')
            return
        print('CREATING DATABASE FILE: ' + database)

    # create transaction manager boilerplate (golang only — same setup every project)
    if args.language == 'golang':
        tx_manager = functions.create_tx_manager(args)
        if tx_manager != 'DONE':
            print('PROBLEM CREATING TRANSACTION MANAGER INTERFACE FILE')
            return
        print('CREATING TRANSACTION MANAGER INTERFACE FILE: ' + tx_manager)

        transaction = functions.create_transaction(args)
        if transaction != 'DONE':
            print('PROBLEM CREATING TRANSACTION FILE')
            return
        print('CREATING TRANSACTION FILE: ' + transaction)

    # create logger boilerplate (golang only — same setup every project)
    if args.language == 'golang':
        logger = functions.create_logger(args)
        if logger != 'DONE':
            print('PROBLEM CREATING LOGGER FILE')
            return
        print('CREATING LOGGER FILE: ' + logger)

    # create a filled-in health resource + the router that wires it up
    # (golang only, --initial-setup only)
    if args.language == 'golang' and getattr(args, 'initial_setup', False):
        health = functions.create_health(args)
        if health != 'DONE':
            print('PROBLEM CREATING HEALTH RESOURCE')
            return
        print('CREATING HEALTH RESOURCE: ' + health)

        router = functions.create_router(args)
        if router != 'DONE':
            print('PROBLEM CREATING ROUTER FILE')
            return
        print('CREATING ROUTER FILE: ' + router)

    # create docker files
    if args.docker:
        dockerfile = functions.create_dockerfile(args)
        if dockerfile != 'DONE':
            print('PROBLEM CREATING DOCKERFILES')
            return
        print('CREATING DOCKER FILES: ' + dockerfile)

    # install dependencies (--initial-setup implies this — a filled-in health
    # resource that doesn't compile because its deps were never fetched
    # defeats the point)
    if args.requirements or getattr(args, 'initial_setup', False):
        requirements = functions.install_dependencies(args)
        if requirements != 'DONE':
            print('PROBLEM INSTALLING DEPENDENCIES')
            return
        print('INSTALLING REQUIREMENTS:' + requirements)

    # create server file (--initial-setup implies this too — no point wiring
    # config/logger/db/router/health with nothing to actually run them)
    if args.server or getattr(args, 'initial_setup', False):
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

