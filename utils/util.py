import os

# create folders
def create_folders(args):
    unix_folder_paths = [
            '/src', 
            '/src/controller',
            '/src/domain',
            '/src/interfaces',
            '/src/interfaces/interactor',
            '/src/repository',
            '/src/model'
            ]

    list_of_directory = os.listdir("./")
    dir_already_exists = False

    for dir_name in list_of_directory:
        if dir_name == args.project_dir:
            dir_already_exists = True
            print("YOU CANNOT USE " + args.project_dir + " AS YOUR DIRECTORY NAME BECAUSE IT ALREADY EXISTS")
            return

    # create the root folder
    if dir_already_exists == False:
        print("CREATING THE ROOT DIRECTORY")
        os.mkdir("./" + args.project_dir)

    # create all the folders
    for path in unix_folder_paths:
        print("CREATING " + "./" + args.project_dir + path)
        os.mkdir("./" + args.project_dir + path)

    if args.docker:
        os.mkdir("./" + args.project_dir + "/docker")

    return 'ok'

# create files
def create_files(args):
    if args.language == "typescript":
        os.chdir("./" + args.project_dir)
        os.system("git init")
        os.system("npm i typescript --save-dev")
        os.system("npx tsc --init")
        return 'ok'
     
    if args.language == "golang":
        os.chdir("./" + args.project_dir)
        os.system("git init") # in the future could add the remote repository if given
        os.system("go mod init " + args.project_dir)
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
