# CodeSeed
CodeSeed is a script that automates the creation of the folder structure of your backend API. 
It creates all the files and folders necessary so you can jump right in and start working on 
your backend project. Currently it only supports two languages (golang and typescript).

The name CodeSeed comes from the fact that this script helps you seed our backend API 
that will later grow to be your project.

Happy Hacking!!


## Contents
- [Requirements](#requirements)
- [Installation](#installation)
    - [The Easy Way](#the-easy-way)
    - [Manually](#manually)
        - [Linux && Darwin](#linux--darwin)
        - [Windows](#windows)
- [Usage](#usage)
- [Options](#options)

## Requirements
You will require the following to use codeseed
- Nodejs
- NPM
- Golang

> [!NOTE] *If you are only going to be using Typescript for your project then you will only need Nodejs and NPM. The same goes for golang*

The following is required for manual installation
- Python3
- Pip3

## Installation


### The Easy Way
The easiest way to use CodeSeed is to download OS specific binary from the latest release and add the 
path to the binary in your `rc` file or if you are on windows, add the path of the codeseed binary to the Environment variables.

```sh
 export PATH="$HOME/.codeseed:$PATH" 
 ```
### Manually

#### Linux && Darwin
To manually install codeseed you need to have python installed on your computer. Once you have confirmed 
that you have python installed, you can then clone the codeseed repository and run the `install.sh` file inside of it.
```sh
git clone https://github.com/sabi1125/CodeSeed.git
```
The `install.sh` script will create a `~/.codeseed` binary, you will have to export this path in your `rc` file like the following.

```sh
 export PATH="$HOME/.codeseed:$PATH" 
 ```

#### Windows
Currently the `install.sh` only works with unix like systems for windows run `python3 -m PyInstaller --onefile --add-data "templates;templates" codeseed.py`
this will create a `dist` folder. Add the path to the `dist` folder to your Environment variables and restart your machine and you are good to go.

> [!NOTE] *The `--add-data` flag is required — codeseed's generated file content lives in `templates/`, not hardcoded in the script, so the binary needs it bundled to work.*

## Usage
Using CodeSeed is very easy. You just need to call codeseed on your terminal and add the name of the Backend project you want to create. Like the following.

```sh
codeseed init <project-name> --options
```
This will create a folder with a Backend project on your local machine. 

The options can be chained if the option do not require an argument like the following.

```sh
codeseed init <project-name> -dras
```

Options like `--language` and `--url` requires a string argument so they cannot be chained.
```sh
codeseed init --language golang --url git@github.com:sabi1125/CodeSeed.git
```

## Argument

| Argument   | Description                                             | Useage                                     |
| ------     | ------------------------------------------------------- | ------------------------------------------ |
| init       | Creates new project                                     | `codeseed init <project-name> --<options>` |
| create     | Creates the controller, interactor and repository files (golang: plus their `inputport` interfaces and `entities`) | `codeseed create <filename>` |
| remove     | Deletes a resource's layer files (golang only)          | `codeseed remove [<name>]`                 |
| update     | Renames a resource's files and identifiers (golang only)| `codeseed update [--from <name>] [--to <new-name>]` |

### Project layout by language

**typescript** keeps the original flat layout: everything under `src/` (`src/controller`, `src/repository`, `src/interfaces/interactor`, ...).

**golang** does not use a `src/` layer — `go.mod` and `cmd/<project-name>/main.go` live at the project root, matching normal Go convention:

```
cmd/<project-name>/main.go
internal/
  controller/
  domain/
    entities/
    interactor/
      inputport/
        mock/
    repository/
      inputport/
        mock/
  infrastructure/
  response/
  log/           # generated logger.go — zap, configured via LOG_LEVEL/APP_ENV env vars
  util/
```

`codeseed create <name>` fills in a struct + constructor + empty interface per layer — method bodies are yours to write, not generated. The `inputport/` files carry a `go:generate mockgen` directive (`go.uber.org/mock`) so a mock is one `go generate ./...` away once the interface has methods on it.

`internal/infrastructure/` is generated with a `database.go` (GORM + MySQL connection via `DB_*` env vars) on every golang init.

### remove and update (golang only)

`codeseed create` tracks the last 5 resource names in `.codeseed.json` (`recent_resources`), so `remove` and `update` don't require retyping an exact name — run them with no arguments and pick a number from a list instead:

```sh
codeseed remove
# SELECT A RESOURCE:
#   1) problem
#   2) submission
# Enter number:
```

`codeseed update` renames the layer files for a resource and rewrites the identifiers inside them (`ProblemInteractor` -> `WidgetInteractor`, etc.) — content you've already written in those files is preserved, only the exact old identifiers get swapped. It does **not** chase references to the old name in other files (e.g. wiring in `main.go`) — you'll get a note printed if that applies.

Both accept explicit args too, skipping the picker: `codeseed remove <name>`, `codeseed update --from <name> --to <new-name>`.

> [!NOTE] *Only the last 5 created resources are tracked — anything older still exists on disk, you just have to pass its name explicitly instead of picking it from the list.*

## Options
### Init argument options:
| Option          | ShortHand | Description                                                                                             |
| ------          | --------- | -----------                                                                                             |
| --language      | -l        | select the language you want your project to be setup in.(options[golang, typescript])                  |
| --docker        | -d        | creates dockerfile and docker-compose.yml file for your project                                         |
| --requirements  | -r        | requirements installs the packages(dependencies) that is required for the project                       |
| --actions       | -a        | creates a github actions folder and file                                                                |
| --server        | -s        | creates the server file for the language you have selected                                              |
| --url           | -u        | adds the remote github repository for the new project                                                   |
| --ignore-config | N/A       | specify the ignore files you dont want to create(options[docker, git])                                  |

### Create argument options:
| Option           | ShortHand | Description                                                                                                           |
| ------           | --------- | -----------                                                                                                           |
| --with-test      | N/A       | when stated creates test files for all the layers for the said file of files `codeseed <filename> --with-test`        |

> [!NOTE] *The create argument does not have any options*

If no language is selected when creating the project directory with -s or -r then the default language will be selected.

> [!NOTE] *The default language is Typescript*
