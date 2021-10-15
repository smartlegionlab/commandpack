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


class CommandExecutorBase(ABC):
    """Abstract Command Executor."""

    def execute(self, command: str):
        """
        Command execute.

        :param command: <str> - command.
        :return: <bool> inverted boolean status of execution by _execute command.

        """
        return not bool(self._execute(command))

    @abstractmethod
    def _execute(self, command: str):
        """
        Command execute.

        :param command: <str> - command.
        :return: status of execution command.

        """

    def __call__(self, command: str):
        return self.execute(command)


class SubCommandExecutor(CommandExecutorBase):
    """Command executor with subprocess."""

    def _execute(self, command: str):
        """
        Command execute.

        :param command: <str> - command.
        :return: status of execution command.

        """
        p = subprocess.Popen(command, shell=True,
                             stderr=subprocess.DEVNULL)
        status = p.wait()
        return status


class OsCommandExecutor(CommandExecutorBase):
    """Command executor with os.system."""
    def _execute(self, command: str):
        """
        Command execute.

        :param command: <str> - command.
        :return: status of execution command.
        """
        status = os.system(command)
        return status


class ExecutorsFactoryBase:
    """Abstract Executors Factory."""

    @classmethod
    def get_os_executor(cls):
        """Get os command executor"""

    @classmethod
    def get_sub_executor(cls):
        """Get sub command executor"""

    @classmethod
    def smart_get_executor(cls):
        """
        Smart command executor.

        Returns the executor depending on the system.

        """


class ExecutorsFactory:
    """Executors Factory."""

    @classmethod
    def get_os_executor(cls):
        """Get os command executor"""
        return OsCommandExecutor()

    @classmethod
    def get_sub_executor(cls):
        """Get sub command executor"""
        return SubCommandExecutor()

    @classmethod
    def smart_get_executor(cls):
        """
        Smart command executor.

        Returns the executor depending on the system.

        """
        if os.name == 'posix':
            return cls.get_sub_executor()
        else:
            return cls.get_os_executor()


class CommandExecutor:
    """Command Executor.

    Cross-platform.

    Uses the executor depending on the system.
    """
    def __init__(self):
        self._executor = self._get_executor()

    def execute(self, command):
        """
        Command execute.

        :param command: - command.
        :return: status of execution command.

        """
        return self._executor(command)

    @staticmethod
    def _get_executor():
        """
        Get executor.

        :return: - returns the executor depending on the system.

        """
        return ExecutorsFactory().smart_get_executor()

    def __call__(self, command):
        return self._executor(command)


def os_execute(command: str):
    """
    Uses command executor with os.system.

    :param command: <str> - command.
    :return: status of execution command.
    """
    executor = OsCommandExecutor()
    return executor(command)


def sub_execute(command):
    """
    Uses command executor with subprocess.

    :param command: <str> - command.
    :return: status of execution command.
    """
    executor = SubCommandExecutor()
    return executor(command)


def smart_execute(command):
    """
    Uses command executor depending on the system.

    :param command:
    :return: status of execution command.

    """
    executor = CommandExecutor()
    return executor(command)
