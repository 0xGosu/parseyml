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

To allow reading default enviroment file use this command:
`parseyml .env docker-compose.yml COMPOSE`

Then run this command to excute export script immediately
`eval $(parseyml docker-compose.yml COMPOSE)`
`eval $(parseyml .env docker-compose.yml COMPOSE)`

Another usage is parse yaml file via pipeline

`cat appspec.yml | parseyml APPSPEC`

`eval $(cat appspec.yml | parseyml APPSPEC)`

There is also an option to export yaml data to json via this command:

`parseyml .env docker-compose.yml json`

## Shell enviroment variable subsitution:

Shell enviroment variable can be used in the .yml file as follow: config.yml
``` 
AMQP_URI: pyamqp://${PYAMQP_URL:rbmqu:rbmqp@rabbitamqp:5672/local}
WEB_SERVER_ADDRESS: '${HOST}:${PORT}'
```
`eval $(cat config.yml | parseyml CONFIG)` will give you value of AMQP_URI as `CONFIG__AMQP_URI`
Note: `${ENV_KEY_NAME:ENV_DEFAULT_VALUE}`
