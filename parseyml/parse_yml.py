# !/usr/bin/python
# -*- coding: utf-8 -*-
#
#  parse_yml.py
#
#
#  Created by TVA on 6/17/16.
#  Copyright (c) 2016 parseyml. All rights reserved.
#
from __future__ import unicode_literals
import os, sys, yaml, re


def travel_and_print_env(data, root_key=''):
    if isinstance(data, dict):
        for key in data:
            if root_key:
                cur_key = root_key + '__' + key
            item = data[key];
            if isinstance(item, dict) or isinstance(item, list):
                travel_and_print_env(item, root_key=cur_key);
            else:
                sys.stdout.write("export %s='%s'\n" % (cur_key.upper(), item))
    else:
        for i in range(len(data)):
            cur_key = root_key + '_%s_' % i
            item = data[i]
            if isinstance(item, dict) or isinstance(item, list):
                travel_and_print_env(item, root_key=cur_key);
            else:
                sys.stdout.write("export %s='%s'\n" % (cur_key.upper(), item))


def validate_root_key(root_key):
    m = re.match(r'^[a-zA-Z]\w*$', root_key)
    return m is not None


def main(argv):
    args = argv[1:]
    if len(args) == 2:  # read yml from file
        filePath, root_key = args
        with open(filePath) as f:
            data = yaml.load(f);
            if not validate_root_key(root_key):
                sys.stderr.write("invalid root_key example: 'ROOT_KEY'")
                return 1
            travel_and_print_env(data, root_key=root_key.strip().upper());
    elif len(args) == 1:  # read yml from pipe line
        root_key = args[0]
        if not validate_root_key(root_key):
            sys.stderr.write("invalid root_key example: 'ROOT_KEY'")
            return 1
        data = yaml.load(sys.stdin.read())
        travel_and_print_env(data, root_key=root_key.strip().upper());

    return 0

if __name__ == '__main__':
    result = main(sys.argv)
    if result == 0:
        sys.stdout.write("# Run this command to configure your shell:\n")
        sys.stdout.write("# eval $(python %s)\n" % ' '.join(sys.argv))
    sys.exit(result)
