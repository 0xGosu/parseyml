# parseyml
Tool to parse yaml .yml file and export to shell environment


| Branch  | Build status                             |
| ------- | ---------------------------------------- |
| master  | [![Build Status](https://travis-ci.org/tranvietanh1991/parseyml.svg?branch=master)](https://travis-ci.org/tranvietanh1991/parseyml) |
| develop | |

## Installation:

### via pypi:
`pip install parseyml`

### via setup.py
`python setup.py install`


## Usage:

Run this command on your shell:

`parseyml docker-compose.yml COMPOSE`

All of docker-compose file content will be transcript to bash export script

Or run this command to excute export script immediately
`eval $(parseyml docker-compose.yml COMPOSE)`

Another usage is parse yaml file via pipeline

`cat appspec.yml | parseyml APPSPEC`

`eval $(cat appspec.yml | parseyml APPSPEC)`