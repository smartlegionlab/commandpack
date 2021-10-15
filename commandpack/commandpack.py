# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Module for working with commands"""
import os
from abc import ABC, abstractmethod


class CommandBase(ABC):
    """Abstract command"""

    @abstractmethod
    def execute(self, executor):
        """Execute command"""


class Command(CommandBase):
    """Command"""
    def __init__(self, name):
        self._name = str(name)

    def execute(self, executor=None) -> bool:
        """
        Running a command to execute.

        :param executor: - the object that executes the commands.
        :return: - logical status of the command execution.

        """
        if executor is None:
            return not os.system(self._name)
        return executor.execute(self._name)

    @property
    def name(self):
        """Command as a string"""
        return self._name

    def __repr__(self):
        return f'{self._name}'

    def __call__(self, executor=None):
        return self.execute(executor)


class PackBase(ABC):
    """Abstract Command Package"""

    @abstractmethod
    def add(self, command):
        """
        Add a command.

        :param command: - Command object.
        :return: None.

        """

    @abstractmethod
    def add_commands(self, commands):
        """
        Add Commands.

        :param commands: iterator with Command objects.
        :return: None

        """

    @abstractmethod
    def remove(self, command: Command):
        """
        Remove command.

        :param command: - Command object.
        :return: None

        """

    @abstractmethod
    def get_commands(self):
        """
        Get all the commands from the package.

        :return: - generator with command objects.

        """

    @abstractmethod
    def execute(self, executor=None):
        """
        Generator, starts the execution of commands,
        returning logical execution statuses.

        :param executor: - CommandExecutor object.
        :return: - returning logical execution statuses.
        """


class Pack(PackBase):
    """Command Package"""
    def __init__(self, name):
        self._commands = []
        self._name = str(name)

    def add(self, command: Command):
        """
        Add a command.

        :param command: - Command object.
        :return: None.

        """
        if not isinstance(command, Command):
            raise TypeError
        self._commands.append(command)

    def add_commands(self, commands):
        """
        Add Commands.

        :param commands: iterator with Command objects.
        :return: None

        """
        for command in commands:
            if isinstance(command, Command):
                self.add(command)

    def remove(self, command: Command):
        """
        Remove command.

        :param command: - Command object.
        :return: None

        """
        if command in self._commands:
            index = self._commands.index(command)
            del self._commands[index]

    def get_commands(self):
        """
        Get all the commands from the package.

        :return: - generator with command objects.

        """
        return (command for command in self._commands)

    def execute(self, executor=None):
        """
        Generator, starts the execution of commands,
        returning logical execution statuses.

        :param executor: - CommandExecutor object.
        :return: - returning logical execution statuses.
        """
        for command in self._commands:
            if executor is None:
                yield command.execute()
            else:
                yield command.execute(executor)

    @property
    def commands(self):
        """Commands list"""
        return self._commands

    @property
    def name(self):
        """Pack name"""
        return self._name

    @property
    def count(self):
        """Commands count"""
        return len(self._commands)

    def __repr__(self):
        return f'{self._name}'

    def __call__(self):
        return self.execute()


class CommandPackFactory:
    """Command and Pack factory"""
    @classmethod
    def create_command(cls, name):
        """Create command with name: name"""
        return Command(name)

    @classmethod
    def create_pack(cls, name):
        """Create pack with name: name"""
        return Pack(name)
