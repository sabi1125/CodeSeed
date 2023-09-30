import os


# create folders
def create_folders(args):
    unix_folder_paths = [
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
        if dir_name == args.project_dir:
            dir_already_exists = True
            print('YOU CANNOT USE ' + args.project_dir + ' AS YOUR DIRECTORY NAME BECAUSE IT ALREADY EXISTS')
            return

    # create the root folder
    if dir_already_exists == False:
        print('CREATING THE ROOT DIRECTORY')
        os.mkdir('./' + args.project_dir)

    # create all the folders
    for path in unix_folder_paths:
        print('CREATING ' + './' + args.project_dir + path)
        os.mkdir('./' + args.project_dir + path)

    if args.docker:
        os.mkdir('./' + args.project_dir + '/docker')

    return 'ok'

# create files
def create_files(args):
    if args.language == 'typescript':
        os.chdir('./' + args.project_dir)
        os.system('git init')
        os.chdir('./src')
        os.system('npm i typescript --save-dev')
        os.system('npx tsc --init')
        os.chdir('..')
        return 'ok'
     
    if args.language == 'golang':
        os.chdir('./' + args.project_dir)
        os.system('git init')
        os.chdir('./src')
        os.system('go mod init ' + args.project_dir)
        os.chdir('..')
        return 'ok'


    return 'UNEXPECTED ERROR ENCOUNTERED'


# create dockerfile
def create_dockerfile(args):
    docker_compose_file = open('docker-compose.yml', 'x')
    docker_compose_file.write('#write your docker compose file here')
    docker_compose_file.close()
    os.chdir('docker')

    dockerfile = open('DOCKERFILE', 'x')
    dockerfile.write('#write you dockerfile here')
    dockerfile.close()
    os.chdir('..')
    return 'ok'

# create serverfile
def create_server(args):
    if args.language == 'typescript':
        os.chdir('src')
        file = open('server.ts', 'x')
        file.write('// server file')
        file.close()
        os.chdir('..')
        return 'ok'

    if args.language == 'golang':
        os.chdir('src')
        file = open('server.go', 'x')
        file.write('// server file')
        file.close()
        os.chdir('..')
        return 'ok'

    return 'UNEXPECTED ERROR ENCOUNTERED'

# create actions
def create_actions(args):
    os.mkdir('.github')
    os.mkdir('.github/workflows')
    os.chdir('.github/workflows')
    file = open('actions.yml', 'x')
    file.write('# your github-actions go here')
    file.close()
    os.chdir('..')
    os.chdir('..')

    return 'ok'

# install dependencies
def install_dependencies(args):
    if args.language == 'typescript':
        os.chdir('./src')
        dependencies = [
                'npm install express', 
                'npm install @types/express',
                'npm install ts-node', 
                'npm install ts-dotenv',
                'npm install cors', 
                'npm install winston',
                'npm install helmet'
                ]
        for items in dependencies:
            os.system(items)

        os.chdir('..')
        return 'ok'

    if args.language == 'golang':
        os.chdir('./src')
        dependencies = [
                'go get -u github.com/labstack/echo/v4',
                'go get -u github.com/francoispqt/onelog',
                'go get -u gorm.io/gorm'
                ]
        for items in dependencies:
            os.system(items)

        os.chdir('..')
        return 'ok'

    return 'UNEXPECTED ERROR ENCOUNTERED'

