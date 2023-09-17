# CodeSeed
CodeSeed is a script that automates the creation of the file structure of your backend API. It creates all the files and folders necessary so you can jump right in and start working on your backend project. Currently it only supports two languages (golang and typescript) but the next version will support multiple languages.

The name CodeSeed comes from the fact that this script helps you seed our backend API that will later grow to be your project.

Happy Hacking!!


## Contents
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)

## Installation
This script works for both Widows and Unix systems. To install the codeseed first clone codeseed to your device with the following command.

```
git clone https://github.com/sabi1125/CodeSeed.git
```
### The Easy
The easiest way to use CodeSeed is to download OS specific binary from the latest release and add the path to the Environment Variable.
### Darwin
If you have Python3 installed on your local machine then you can use the `install.sh` script that is present in the CodeSeed folder, or alternatively you can just add the path to the dist folder in your `rc` file. If you are using the `install.sh` script then be sure to use the following command to make the script file an executable.

### Windows
Just clone the github repository and add the path to the dist folder inside of the `CodeSeed` repository to your Environment Variables, restart your computer.

## Usage
Using CodeSeed is very easy. You just need to call codeseed on your terminal and add the name of the Backend project you want to create. Like the following.

```
codeseed <project-name> --options
```
This will make a folder with a Backend project on your local machine. 

> ***Note: The next version will install a basic server that you can make a HTTP request from the browser or just CURL it.*** 

## Options
| Option | ShortHand | Description |
| ------ | --------- | ----------- |
| --language | -l | Select the language you want your project to be setup in. Currently only supports golang and typescript |
| --docker | -d | Creates Dockerfile and docker-compose.yml file for your project |
| --dependencies | -dp | Installs basic dependencies for the language you have selected |
| --actions | -a | Creates a github actions folder and file |
| --server | -s | Creates the server file for the language you have selected |

If no language is selected when creating the project directory with -s or -dp then the default languate will be selected.

> ***Note:  The default language is Typescript***
 
