# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import json
from abc import ABC, abstractmethod
from pathlib import Path

from commandpack.commandpack import Pack, Command


class ParserBase(ABC):
    """Abstract parser"""
    @abstractmethod
    def parse_file(self, file):
        """Parse file"""

    def __call__(self, file):
        return self.parse_file(file)


class CfgParser(ParserBase):

    def parse_file(self, file):
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

    def parse_file(self, file):
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


class SmartParser:
    def __init__(self):
        self._cfg_parser = CfgParser()
        self._json_parser = JsonParser()

    def parse_file(self, file):
        with open(file) as f:
            line = f.readline(1)
        if Path(file).suffix == '.json' or line.startswith('{'):
            return self.parse_json(file=file)
        else:
            return self.parse_cfg(file=file)

    def parse_cfg(self, file):
        return self._cfg_parser(file)

    def parse_json(self, file):
        return self._json_parser(file)

    def __call__(self, file):
        return self.parse_file(file)


class ParsersFactory:
    """Parsers Factory"""

    @classmethod
    def get_cfg_parser(cls):
        return CfgParser()

    @classmethod
    def get_json_parser(cls):
        return JsonParser()


def parse_cfg_file(file):
    cfg_parser = CfgParser()
    return cfg_parser(file)


def parse_json_file(file):
    json_parser = JsonParser()
    return json_parser(file)


def parse_packs(file):
    with open(file) as f:
        line = f.readline(1)
    if Path(file).suffix == '.json' or line.startswith('{'):
        return parse_json_file(file)
    else:
        return parse_cfg_file(file)
