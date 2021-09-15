# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------
import json
import os
from collections import namedtuple

import pytest

from commandpack.commandpack import Command
from commandpack.executors import OsCommandExecutor, SubCommandExecutor, ExecutorsFactory, CommandExecutor, os_execute, \
    sub_execute, smart_execute
from commandpack.parsers import CfgParser, JsonParser, SmartParser, ParsersFactory, parse_cfg_file, parse_json_file, \
    parse_packs


@pytest.fixture(scope='session', name='command')
def get_command():
    return Command('echo "test"')


@pytest.fixture(name='command_name')
def get_command_title():
    return 'echo "test"'


@pytest.fixture(name='os_executor')
def os_executor():
    return OsCommandExecutor()


@pytest.fixture(name='sub_executor')
def sub_executor():
    return SubCommandExecutor()


@pytest.fixture(params=[('echo "Smart Legion!"', True), ('bad_command', False)], name='command_status')
def command(request):
    yield request.param


@pytest.fixture(name='executors_factory')
def get_executors_factory():
    return ExecutorsFactory()


@pytest.fixture(name='os_name', params=['posix', 'win'])
def get_os_names(request):
    yield request.param
    os.name = 'posix'


@pytest.fixture(name='command_executor')
def get_command_executor():
    return CommandExecutor()


@pytest.fixture(name='os_execute_func')
def get_os_execute_func():
    return os_execute


@pytest.fixture(name='sub_execute_func')
def get_sub_execute_func():
    return sub_execute


@pytest.fixture(name='smart_execute_func')
def get_smart_execute_func():
    return smart_execute


@pytest.fixture(name='cfg_parser')
def get_cfg_parser():
    return CfgParser()


@pytest.fixture(name='data')
def get_data():
    data = r"""
[Ubuntu]
echo Ubuntu

[Fedora]
echo Fedora

[Manjaro]
echo Fedora

[default]
echo default
"""
    return data


@pytest.fixture(name='path')
def get_dir(tmpdir, data):
    file = tmpdir.join('file.cfg')
    file.write(data)
    Path = namedtuple('Path', ('file', 'folder'))
    yield Path(file, tmpdir)


@pytest.fixture(name='pack_names')
def get_pack_names():
    return ['Ubuntu', 'Fedora', 'Manjaro', 'default']


@pytest.fixture(name='json_parser')
def get_json_parser():
    return JsonParser()


@pytest.fixture(name='data_json')
def get_data_json():
    data = {
        "Ubuntu":
            [
                'echo Ubuntu1',
                'echo Ubuntu2'
            ],
        "Fedora":
            [
                'echo Fedora1',
                'echo Fedora2'
            ]
    }

    return data


@pytest.fixture(name='file_json')
def get_file_json(tmpdir, data_json):
    file = tmpdir.join('file.json')
    with file.open('w') as f:
        json.dump(data_json, f)
    return file


@pytest.fixture(name='smart_parser')
def get_smart_parser():
    return SmartParser()


@pytest.fixture(name='parsers_factory')
def get_parsers_factory():
    return ParsersFactory()


@pytest.fixture(name='parse_cfg_file')
def get_parse_cfg_file():
    return parse_cfg_file


@pytest.fixture(name='parse_json_file')
def get_parse_json_file():
    return parse_json_file


@pytest.fixture(name='parse_packs')
def get_parse_packs():
    return parse_packs
