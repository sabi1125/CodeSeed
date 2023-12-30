# CodeSeed
CodeSeed is a script that automates the creation of the folder structure of your backend API. It creates all the files and folders necessary so you can jump right in and start working on your backend project. Currently it only supports two languages (golang and typescript).

The name CodeSeed comes from the fact that this script helps you seed our backend API that will later grow to be your project.

Happy Hacking!!


## Contents
- [Installation](#installation)
    - [The Easy Way](#the-easy-way)
    - [Linux && Darwin](#linux--darwin)
    - [Windows](#windows)
- [Usage](#usage)
- [Options](#options)

## Installation

### Manually

### The Easy Way
The easiest way to use CodeSeed is to download OS specific binary from the latest release and add the path to the binary in your `rc` file or if you are on windows, add the path of the codeseed binary to the Environment variables.

### Linux && Darwin
To manually install codeseed you need to have python installed on your computer. Once you have confirmed that you have python installed, you can then clone the codeseed repository and run the `install.sh` file inside of it.
```
git clone https://github.com/sabi1125/CodeSeed.git
```
The `install.sh` script will create a `~/.codeseed` binary, you will have to export this path in your `rc` file like the following.

```
 export PATH="$HOME/.codeseed:$PATH" 
 ```

### Windows
Currently the `install.sh` only works with unix like systems for windows run `python3 -m PyInstaller --onefile codeseed.py` this will create a `dist` folder. Add the path to the `dist` folder to your Environment variables and restart your machine and you are good to go.

## Usage
Using CodeSeed is very easy. You just need to call codeseed on your terminal and add the name of the Backend project you want to create. Like the following.

```
codeseed init <project-name> --options
```
This will create a folder with a Backend project on your local machine. 

The options can be chained if the option do not require an argument like the following.

```
codeseed init <project-name> -dras
```

Options like `--language` and `--url` requires a string argument so they cannot be chained.
```
codeseed init --language golang --url git@github.com:sabi1125/CodeSeed.git
```

## Argument

| Argument   | Description | Useage |
| ------     | ----------- | ------ |
| init       | Creates new project | `codeseed init <project-name> --<options>` |
| create     | Creates the controller, interactor and repository files | `codeseed create <filename>`  |

## Options
### Init argument options:
| Option         | ShortHand | Description                                                                                             |
| ------         | --------- | -----------                                                                                             |
| --language     | -l        | Select the language you want your project to be setup in. Currently only supports golang and typescript |
| --docker       | -d        | Creates Dockerfile and docker-compose.yml file for your project                                         |
| --requirements | -r        | REQUIREMENTS INSTALLS THE PACKAGES(DEPENDENCIES) THAT IS REQUIRED FOR THE PROJECT                       |
| --actions      | -a        | Creates a github actions folder and file                                                                |
| --server       | -s        | Creates the server file for the language you have selected                                              |
| --url          | -u        | Adds the remote github repository for the new project                                                   |

> ***Note: The create argument does not have any options***

If no language is selected when creating the project directory with -s or -r then the default languate will be selected.

> ***Note:  The default language is Typescript***
 
