import os

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

    return 'FOLDERS CREATED'

def create_files(language, project_dir):
    if language == "typescript":
        os.chdir("./" + project_dir)
        os.system("git init")
        os.system("npm i typescript --save-dev")
        os.system("npx tsc --init -y")
        return 'FILES CREATED'
     
    if language == "golang":
        os.chdir("./" + project_dir)
        os.system("git init") # in the future could add the remote repository if given
        os.system("go mod init " + project_dir)
        return 'FILES CREATED'
    
    return 'UNEXPECTED ERROR ENCOUNTERED'

