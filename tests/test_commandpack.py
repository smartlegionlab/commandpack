# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest

from commandpack.commandpack import Command, Pack


class TestCommand:
    def test_name(self, command, command_name):
        assert command.name == command_name

    def test_execute(self, command, os_executor, sub_executor):
        assert command.execute()
        assert command.execute(os_executor)
        assert command.execute(sub_executor)

    def test_str_(self, command, command_name):
        assert str(command) == f'{command_name}'

    def test_call_(self, command):
        assert command()


class TestPack:

    def test_str(self, pack, pack_name):
        assert str(pack) == f'{pack_name}'

    def test_commands(self, pack):
        assert isinstance(pack.commands, list)

    def test_add(self, pack, command):
        pack.add(command)
        assert command in pack._commands

    def test_add_bad_types(self, pack):
        with pytest.raises(TypeError):
            pack.add(8)

    def test_add_commands(self, pack, commands):
        pack.add_commands(commands)
        name_list = [comm for comm in pack.get_commands()]
        assert all([c in name_list for c in commands])

    def test_remove(self, pack, command):
        pack.add(command)
        pack.remove(command)
        assert command not in pack._commands

    def test_get_commands(self, pack, command):
        pack.add(command)
        assert command in [c for c in pack.get_commands()]

    def test_name(self, pack):
        assert pack.name == 'Termux'

    def test_count(self, pack, commands):
        pack.add_commands(commands)
        assert len(commands) == pack.count

    def test_execute(self, commands, pack, os_executor, sub_executor):
        pack.add_commands(commands)
        assert all([status for status in pack.execute()])
        assert all([status for status in pack.execute(os_executor)])

    def test_call_(self, pack, commands):
        pack.add_commands(commands)
        assert all([status for status in pack()])


class TestCommandPackFactory:
    def test_create_command(self, command_pack_factory):
        assert isinstance(command_pack_factory.create_command('new'), Command)

    def test_create_pack(self, command_pack_factory):
        assert isinstance(command_pack_factory.create_pack('new'), Pack)


@pytest.fixture(name='commands')
def get_commands():
    commands = (Command('echo 1'), Command('echo 2'), Command('echo 3'))
    return commands


@pytest.fixture(name='pack_name')
def get_pack_name():
    return 'Termux'
