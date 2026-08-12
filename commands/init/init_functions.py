import os
import json

from utils import templates

def create_dotfiles(args):
    config = {
        "language": args.language,
        "root": os.getcwd(),
        "remote": args.url,
        "recent_resources": [],
    }
    with open('.codeseed.json', "w") as json_file:
        json.dump(config, json_file, indent=4)  # indent is optional, but it makes the file more readable

    return 'DONE'

# create folders
def create_folders(args):
    if args.language == 'golang':
        # golang doesn't use a src/ layer — go.mod and cmd/ live at project root.
        # domain/interactor and domain/repository each carry an inputport/ (the
        # interface the layer above depends on, not the concrete type) plus an
        # inputport/mock/ for generated mocks — dependency inversion, not just
        # controller/interactor/repository as flat siblings.
        folder_paths = [
            '/cmd',
            '/cmd/' + args.foldername,
            '/internal',
            '/internal/controller',
            '/internal/domain',
            '/internal/domain/entities',
            '/internal/domain/interactor',
            '/internal/domain/interactor/inputport',
            '/internal/domain/interactor/inputport/mock',
            '/internal/domain/repository',
            '/internal/domain/repository/inputport',
            '/internal/domain/repository/inputport/mock',
            '/internal/infrastructure',
            '/internal/response',
            '/internal/log',
            '/internal/tx',
            '/internal/util'
        ]
        if getattr(args, 'initial_setup', False):
            folder_paths.append('/internal/config')
    else:
        folder_paths = [
            '/src',
            '/src/controller',
            '/src/domain',
            '/src/interfaces',
            '/src/infrastructure',
            '/src/interfaces/interactor',
            '/src/repository',
            '/src/model'
        ]

    list_of_directory = os.listdir("./")
    dir_already_exists = False

    for dir_name in list_of_directory:
        if dir_name == args.foldername:
            dir_already_exists = True
            print('YOU CANNOT USE ' + args.foldername + ' AS YOUR DIRECTORY NAME BECAUSE IT ALREADY EXISTS')
            return

    # create the root folder
    if dir_already_exists == False:
        print('CREATING THE ROOT DIRECTORY')
        os.mkdir('./' + args.foldername)

    # create all the folders
    for path in folder_paths:
        print('CREATING ' + './' + args.foldername + path)
        os.mkdir('./' + args.foldername + path)

    if args.docker:
        os.mkdir('./' + args.foldername + '/docker')

    return 'DONE'

# create files
def create_files(args):
    os.chdir('./' + args.foldername)
    os.system('git init')
    os.system('git branch -M main')

    # creating gitignore file
    if 'git' in args.ignoreconfig:
        print("CREATING: gitignore")
        if args.language == 'golang':
            gitignore_content = templates.render('golang/gitignore.tmpl', foldername=args.foldername)
        else:
            gitignore_content = templates.render('typescript/gitignore.tmpl')
        with open('.gitignore', "w") as file:
            file.write(gitignore_content)

    if args.language == 'typescript':
        os.chdir('./src')
        os.system('npm i typescript --save-dev')
        os.system('npx tsc --init')
        os.chdir('..')
        return 'DONE'


    if args.language == 'golang':
        os.system('go mod init ' + args.foldername)
        return 'DONE'


    return 'UNEXPECTED ERROR ENCOUNTERED'


# create logger boilerplate (golang only — same setup every project).
# --initial-setup gets the config-aware variant (Init takes a *config.ZapConfig,
# plus MiddlewareLogger) instead of the default env-parsing-only one.
def create_logger(args):
    template = 'golang/logger_with_config.go.tmpl' if getattr(args, 'initial_setup', False) else 'golang/logger.go.tmpl'
    vars = {'module': args.foldername} if getattr(args, 'initial_setup', False) else {}
    with open('internal/log/logger.go', 'x') as file:
        file.write(templates.render(template, **vars))
    return 'DONE'


# create dockerfile
def create_dockerfile(args):
    docker_compose_file = open('docker-compose.yml', 'x')
    docker_compose_file.write(templates.render('shared/docker-compose.yml.tmpl'))
    docker_compose_file.close()
    os.chdir('docker')

    if args.language == 'golang':
        dockerfile_content = templates.render('golang/Dockerfile.tmpl', foldername=args.foldername)
    else:
        dockerfile_content = templates.render('typescript/Dockerfile.tmpl')

    dockerfile = open('DOCKERFILE', 'x')
    dockerfile.write(dockerfile_content)
    dockerfile.close()
    os.chdir('..')
    if 'docker' in args.ignoreconfig:
        print("CREATING: dockerignore")
        with open('.dockerignore', "w"):
            pass
    os.mkdir('scripts')
    os.chdir('scripts')
    file = open('entrypoint.sh', 'x')
    file.write(templates.render('shared/entrypoint.sh.tmpl'))
    file.close()
    os.chdir('..')
    return 'DONE'

# create database connection boilerplate (golang only). --initial-setup gets
# the config-aware variant (Connection takes a *config.DBConfig, Fatals on
# failure) instead of the default raw-env-parsing one.
def create_database(args):
    template = 'golang/database_with_config.go.tmpl' if getattr(args, 'initial_setup', False) else 'golang/database.go.tmpl'
    vars = {'module': args.foldername} if getattr(args, 'initial_setup', False) else {}
    with open('internal/infrastructure/database.go', 'x') as file:
        file.write(templates.render(template, **vars))
    return 'DONE'

# create transaction manager boilerplate (golang only). Manager lives in its
# own internal/tx package (interface only) so the domain layer can depend on
# it without importing internal/infrastructure — same split as
# interactor/repository inputport.
def create_tx_manager(args):
    with open('internal/tx/manager.go', 'x') as file:
        file.write(templates.render('golang/tx_manager.go.tmpl'))
    return 'DONE'


def create_transaction(args):
    with open('internal/infrastructure/transaction.go', 'x') as file:
        file.write(templates.render('golang/transaction.go.tmpl', module=args.foldername))
    return 'DONE'


# create config boilerplate (golang only, --initial-setup only). Env loading
# and validation (Load/LoadDbConfig/LoadZapConfig) — logger.go and
# database.go's config-aware variants depend on the types defined here.
def create_config(args):
    with open('internal/config/config.go', 'x') as file:
        file.write(templates.render('golang/config.go.tmpl'))
    with open('internal/config/config_test.go', 'x') as file:
        file.write(templates.render('golang/config_test.go.tmpl'))
    return 'DONE'


# create router boilerplate (golang only, --initial-setup only). Composition
# root — wires the health resource's repository/interactor/controller
# together and mounts it on the Echo instance passed in from main.go.
def create_router(args):
    with open('internal/infrastructure/router.go', 'x') as file:
        file.write(templates.render('golang/router.go.tmpl', module=args.foldername))
    return 'DONE'


# create a filled-in health resource (golang only, --initial-setup only) —
# unlike `codeseed create <name>`, these aren't empty stubs: a real /health
# route that exercises every layer (controller -> interactor -> repository),
# so --initial-setup produces something you can actually curl right after.
def create_health(args):
    targets = [
        ('internal/domain/entities/health.go', 'golang/health_entity.go.tmpl', {}),
        ('internal/domain/repository/inputport/health_repository_inputport.go', 'golang/health_repository_inputport.go.tmpl', {}),
        ('internal/domain/repository/health_repository.go', 'golang/health_repository.go.tmpl', {'module': args.foldername}),
        ('internal/domain/interactor/inputport/health_interactor_inputport.go', 'golang/health_interactor_inputport.go.tmpl', {}),
        ('internal/domain/interactor/health_interactor.go', 'golang/health_interactor.go.tmpl', {'module': args.foldername}),
        ('internal/controller/health_controller.go', 'golang/health_controller.go.tmpl', {'module': args.foldername}),
    ]
    for path, template, vars in targets:
        with open(path, 'x') as file:
            file.write(templates.render(template, **vars))
    return 'DONE'

# create serverfile. --initial-setup gets the variant wired to config/logger/
# database/router instead of the bare Echo hello-world.
def create_server(args):
    if args.language == 'golang':
        template = 'golang/main_initial_setup.go.tmpl' if getattr(args, 'initial_setup', False) else 'golang/main.go.tmpl'
        os.chdir('cmd/' + args.foldername)
        with open('main.go', 'x') as file:
            file.write(templates.render(template, module=args.foldername))
        os.chdir('../..')
        return 'DONE'

    os.chdir('src')
    if args.language == 'typescript':

        file = open('server.ts', 'x')
        file.write(templates.render('typescript/server.ts.tmpl'))
        file.close()
        os.chdir('..')
        return 'DONE'

    return 'UNEXPECTED ERROR ENCOUNTERED'

# create actions
def create_actions(args):
    os.mkdir('.github')
    os.mkdir('.github/workflows')
    os.chdir('.github/workflows')
    file = open('actions.yml', 'x')
    file.write(templates.render('shared/actions.yml.tmpl'))
    file.close()
    os.chdir('..')
    os.chdir('..')

    return 'DONE'

# install dependencies
def install_dependencies(args):
    if args.language == 'golang':
        # TODO: getting dependencies from user
        dependencies = [
            'github.com/labstack/echo/v4',
            'github.com/francoispqt/onelog',
            'gorm.io/gorm',
            'gorm.io/driver/mysql',
            'go.uber.org/zap'
        ]
        if getattr(args, 'initial_setup', False):
            # config.go (--initial-setup only) needs godotenv to load .env
            dependencies.append('github.com/joho/godotenv')
        for items in dependencies:
            os.system('go get -u ' + items)

        return 'DONE'

    os.chdir('./src')
    if args.language == 'typescript':
        # TODO: getting dependencies from user
        dependencies = [
            'express',
            '@types/express',
            'ts-node',
            'ts-dotenv',
            'cors',
            'winston',
            'helmet'
        ]
        for items in dependencies:
            os.system('npm install ' + items)

        os.chdir('..')
        return 'DONE'

    return 'UNEXPECTED ERROR ENCOUNTERED'

# add remote repository
def add_remote_repository(args):
    command = 'git remote add origin ' + args.url
    print('RUNNING: ' + command)
    os.system(command)
    return 'DONE'
