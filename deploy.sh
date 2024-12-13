#!/bin/bash

CODE_FOLDER=$(dirname $(readlink -f $0))
OPTIONS="-avz --update --exclude=__pycache__ -e ssh"
rsync $OPTIONS ${CODE_FOLDER}/app/ ${AOC24_REMOTE_SERVER}/app
rsync $OPTIONS ${CODE_FOLDER}/src/ ${AOC24_REMOTE_SERVER}/src
