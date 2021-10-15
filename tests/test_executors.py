# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import os

from commandpack.executors import OsCommandExecutor, SubCommandExecutor


class TestOsCommandExecutor:
    def test_execute(self, os_executor, command_status):
        command, status = command_status
        assert os_executor.execute(command) == status

    def test_call_(self, os_executor, command_status):
        command, status = command_status
        assert os_executor(command) == status


class TestSubCommandExecutor:

    def test_execute(self, sub_executor, command_status):
        command, status = command_status
        assert sub_executor.execute(command) == status

    def test_call_(self, sub_executor, command_status):
        command, status = command_status
        assert sub_executor(command) == status


class TestExecutorsFactory:
    def test_get_os_executor(self, executors_factory):
        assert isinstance(executors_factory.get_os_executor(), OsCommandExecutor)

    def test_get_sub_executor(self, executors_factory):
        assert isinstance(executors_factory.get_sub_executor(), SubCommandExecutor)

    def test_smart_get_executor(self, os_name, executors_factory):
        os.name = os_name
        executor = SubCommandExecutor if os.name == 'posix' else OsCommandExecutor
        assert isinstance(executors_factory.smart_get_executor(), executor)


class TestCommandExecutor:
    def test_execute(self, command_executor, command_status):
        command, status = command_status
        assert command_executor.execute(command) == status


def test_os_execute(os_execute_func, command_status):
    command, status = command_status
    assert os_execute_func(command) == status


def test_sub_execute(sub_execute_func, command_status):
    command, status = command_status
    assert sub_execute_func(command) == status


def test_smart_execute(smart_execute_func, command_status):
    command, status = command_status
    assert smart_execute_func(command) == status
