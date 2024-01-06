import os
import json

def create_dotfiles(args):
    config = {
        "language": args.language,
        "root": os.getcwd(),
        "remote": args.url,
    }
    with open('.codeseed.json', "w") as json_file:
        json.dump(config, json_file, indent=4)  # indent is optional, but it makes the file more readable

    return 'DONE'

# create folders
def create_folders(args):
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

    # creating gitignore file
    if 'git' not in args.ignoreconfig:
        print("CREATING: gitignore")
        with open('.gitignore', "w"):
            pass
    os.chdir('./src')

    if args.language == 'typescript':
        os.system('npm i typescript --save-dev')
        os.system('npx tsc --init')
        os.chdir('..')
        return 'DONE'
    

    if args.language == 'golang':
        os.system('go mod init ' + args.foldername)
        os.chdir('..')
        return 'DONE'


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
    if 'docker' not in args.ignoreconfig:
        print("CREATING: dockerignore")
        with open('.dockerignore', "w"):
            pass
    os.mkdir('scripts')
    os.chdir('scripts')
    file = open('entrypoint.sh', 'x')
    file.write('// script file')
    file.close()
    os.chdir('..')
    return 'DONE'

# create serverfile
def create_server(args):
    if args.language == 'typescript':
        os.chdir('src')

        file = open('server.ts', 'x')
        server_code = """
import express from 'express';

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
        """
        file.write(server_code)
        file.close()
        os.chdir('..')
        return 'DONE'

    if args.language == 'golang':
        os.chdir('src')
        file = open('server.go', 'x')
        server_code = """
package main

import (
    "net/http"

    "github.com/labstack/echo/v4"
)

func main() {
    // Create an Echo instance
    e := echo.New()

    // Define a route
    e.GET("/", func(c echo.Context) error {
        return c.String(http.StatusOK, "Hello, Echo!")
    })

    // Start the server
    e.Start(":8080")
}
"""
        file.write(server_code) 
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
    file.write('# your github-actions go here')
    file.close()
    os.chdir('..')
    os.chdir('..')

    return 'DONE'

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
        return 'DONE'

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
        return 'DONE'

    return 'UNEXPECTED ERROR ENCOUNTERED'

# add remote repository
def add_remote_repository(args):
    command = 'git remote add origin ' + args.url
    print('RUNNING: ' + command)
    os.system(command)
    return 'DONE'


