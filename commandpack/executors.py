# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tests for executors.py"""
import os
import subprocess
from abc import ABC, abstractmethod


class ExecutorBase(ABC):
    """Abstract Command Executor"""
    @abstractmethod
    def execute(self, command):
        """Execute command"""

    def __call__(self, command):
        return self.execute(command)


class OsExecutor(ExecutorBase):
    def execute(self, command):
        """
        Execute command.

        - To execute the command, os.system is used;

        :param command: <str> - command;
        :return: <bool> - status of execution command.
        """
        return not bool(os.system(command))


class SubExecutor(ExecutorBase):
    def execute(self, command):
        """
        Execute command.

        - To execute the command, subprocess is used;

        WARNING: Use with care, favor OsExecutor;

        :param command: <str> - command;
        :return: <bool> - status of execution command;
        """
        p = subprocess.Popen(command, shell=True, stderr=subprocess.DEVNULL)
        status = p.wait()
        return not bool(status)


class Executor(ExecutorBase):
    os_executor = OsExecutor()
    sub_executor = SubExecutor()

    @classmethod
    def execute(cls, command):
        """
        Execute command.

        - The Executor will be determined automatically, depending on the system.

        :param command: <str> - command;
        :return: <bool> - status of execution command;
        """
        executor = cls._get_executor()
        return executor.execute(command)

    @classmethod
    def _get_executor(cls):
        """
        The Executor will be determined automatically, depending on the system.

        :return: OsExecutor/SubExecutor depending on the posix/another;
        """
        if os.name == 'posix':
            return cls.os_executor
        return cls.sub_executor
