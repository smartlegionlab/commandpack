# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# -------------------------------------------------------
import os

from commandpack.executors import OsExecutor, SubExecutor, Executor


class TestOsExecutor:
    def test_execute(self, os_executor, command_status):
        command, status = command_status
        assert os_executor.execute(command) == status

    def test__call__(self, os_executor, command_status):
        command, status = command_status
        assert os_executor(command) == status


class TestSubExecutor:
    def test_execute(self, sub_executor, command_status):
        command, status = command_status
        assert sub_executor.execute(command) == status

    def test__call__(self, sub_executor, command_status):
        command, status = command_status
        assert sub_executor(command) == status


class TestExecutor:
    def test_execute(self, executor, command_status):
        command, status = command_status
        assert executor.execute(command) == status
        assert executor.os_executor(command) == status
        assert executor.sub_executor(command) == status
        assert executor.sub_executor.execute(command) == status

    def test__get_executor(self, executor, os_executor, sub_executor, os_name):
        os.name = os_name
        if os.name == 'posix':
            assert isinstance(executor._get_executor(), type(os_executor))
        else:
            assert isinstance(executor._get_executor(), type(sub_executor))
