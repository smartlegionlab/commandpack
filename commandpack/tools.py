# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Module for working with commands"""
import json
from abc import ABC, abstractmethod
from pathlib import Path


class Command:
    """Command"""
    def __init__(self, name):
        self._name = str(name)

    @property
    def name(self):
        """Command as a string"""
        return self._name

    def __repr__(self):
        return f'<Command {self._name}>'


class Pack:
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
        return f'<Pack {self._name}>'


class ParserBase(ABC):
    """Abstract parser"""
    @abstractmethod
    def parse(self, file):
        """Parse file"""

    def __call__(self, file):
        return self.parse(file)


class CfgParser(ParserBase):

    def parse(self, file):
        packs = []
        try:
            pack = None
            with open(file, 'r') as f:
                lines = f.readlines()
        except (FileNotFoundError, PermissionError, OSError):
            return []
        else:
            for line in lines:
                line = line.rstrip('\n')
                if (len(line) > 0 and not line.startswith('#')
                        and line.startswith('[') and line.endswith(']')):
                    line = line.rstrip(']').lstrip('[')
                    pack = Pack(str(line))
                    packs.append(pack)
                else:
                    if pack in packs and line:
                        index = packs.index(pack)
                        packs[index].add(Command(str(line)))
        return packs


class JsonParser(ParserBase):

    def parse(self, file):
        packs = []
        try:
            with open(file, 'r') as f:
                json_data = json.load(f)
        except (
                json.decoder.JSONDecodeError,
                FileNotFoundError,
                PermissionError,
                OSError
        ):
            return []
        else:
            for pack_name, commands in json_data.items():
                pack = Pack(pack_name)
                packs.append(pack)
                index = packs.index(pack)
                command_gen = (Command(command) for command in commands if command)
                packs[index].add_commands(command_gen)
            return packs


class Parser(ParserBase):
    cfg = CfgParser()
    json = JsonParser()

    @classmethod
    def parse(cls, file):
        suffix = Path(file).suffix
        parser = cls._get_parser(suffix)
        return parser.parse(file)

    @classmethod
    def _get_parser(cls, suffix):
        if suffix == '.json':
            return cls.json
        return cls.cfg


class PackMaker:
    parser = Parser()

    @classmethod
    def make_pack_list(cls, file, add_list=None, exc_list=None):
        add_list = [] if add_list is None else add_list
        exc_list = [] if exc_list is None else exc_list
        packs = cls.parser.parse(file=file)
        names = [pack.name for pack in packs]
        if add_list:
            name_list = [name for name in add_list if name in names and name not in exc_list]
        else:
            name_list = [name for name in names if name in names and name not in exc_list]
        pack_list = [pack for pack in packs if pack.name in name_list]
        return pack_list
