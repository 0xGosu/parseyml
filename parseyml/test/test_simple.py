#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  test_simple.py
#  
#
#  Created by TVA on 1/28/18.
#  Copyright (c) 2018 parseyml. All rights reserved.
#
from __future__ import unicode_literals
from cStringIO import StringIO
import sys
import re
from parseyml import main
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_case1():
    sys.stdout = mystdout = StringIO()

    main(['parseyml', os.path.join(BASE_DIR, 'test/test_input/docker-compose.yml'), 'COMPOSE'])

    result_stdout = mystdout.getvalue()
    assert len(result_stdout) > 0
    assert "export COMPOSE__SERVICES__WEORDER__IMAGE='registry.gitlab.com/tranvietanh1991/weorder:weoder-restapi-v1.2'" in result_stdout
    assert "export COMPOSE__SERVICES__MYSQLDB__ENVIRONMENT__MYSQL_ROOT_PASSWORD='dummy_password'" in result_stdout
    mystdout.close()
