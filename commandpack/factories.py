# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from commandpack.executors import OsExecutor, Executor, SubExecutor
from commandpack.tools import PackMaker, CfgParser, JsonParser, Parser, Command, Pack


class ExecutorsFactory:
    """Executors factory"""

    @classmethod
    def get_os_executor(cls):
        """Get OsExecutor"""
        return OsExecutor()

    @classmethod
    def get_sub_executor(cls):
        """Get SubExecutor"""
        return SubExecutor()

    @classmethod
    def get_executor(cls):
        """Get Executor"""
        return Executor()


class MakersFactory:

    @classmethod
    def get_pack_maker(cls):
        return PackMaker()


class ParsersFactory:

    @classmethod
    def get_cfg_parser(cls):
        return CfgParser()

    @classmethod
    def get_json_parser(cls):
        return JsonParser()

    @classmethod
    def get_parser(cls):
        return Parser()


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


class ToolsFactory:
    parsers = ParsersFactory()
    command_pack = CommandPackFactory()
    makers = MakersFactory()
    executors = ExecutorsFactory()


class Factory:
    """Main Facility Factory """
    tools = ToolsFactory()
