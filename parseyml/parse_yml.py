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

# Setup YAML parser to check for shell enviroment substituting

ENV_VAR_MATCHER = re.compile(
    r"""
        \$\{       # match characters `${` literally
        ([^}:\s]+) # 1st group: matches any character except `}` or `:`
        :?         # matches the literal `:` character zero or one times
        ([^}]+)?   # 2nd group: matches any character except `}`
        \}         # match character `}` literally
    """, re.VERBOSE
)
IMPLICIT_ENV_VAR_MATCHER = re.compile(
    r"""
        .*          # matches any number of any characters
        \$\{.*\}    # matches any number of any characters
                    # between `${` and `}` literally
        .*          # matches any number of any characters
    """, re.VERBOSE
)


def _replace_env_var(match):
    env_var, default = match.groups()
    return os.environ.get(env_var, default)


def env_var_constructor(loader, node):
    raw_value = loader.construct_scalar(node)
    value = ENV_VAR_MATCHER.sub(_replace_env_var, raw_value)
    return yaml.safe_load(value)


def setup_yaml_parser():
    yaml.add_constructor('!env_var', env_var_constructor)
    yaml.add_implicit_resolver('!env_var', IMPLICIT_ENV_VAR_MATCHER)


# Main logic

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
    setup_yaml_parser()
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
