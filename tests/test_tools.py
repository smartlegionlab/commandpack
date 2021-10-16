# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import pytest


class TestCommand:
    def test_name(self, command):
        assert command.name == 'echo "test"'

    def test__repr__(self, command):
        assert repr(command) == f'<Command {command.name}>'


class TestPack:
    def test_add(self, pack, command):
        pack.add(command)
        assert command in pack.commands

    def test_add_commands(self, pack, commands):
        pack.add_commands(commands)
        assert all([command in pack.commands for command in commands])

    def test_remove(self, pack, commands):
        pack.add_commands(commands)
        command = commands[0]
        assert command in pack.commands
        pack.remove(command)
        assert command not in pack.commands

    def test_get_commands(self, pack, commands):
        command = commands[0]
        pack.add_commands(commands)
        assert command in [c for c in pack.get_commands()]

    def test_commands(self, pack, commands):
        pack.add_commands(commands)
        assert isinstance(pack.commands, list)
        assert commands == pack.commands

    def test_name(self, pack):
        assert pack.name == 'Test'

    def test_count(self, pack, commands):
        pack.add_commands(commands)
        count = len(commands)
        assert pack.count == count

    def test_repr(self, pack):
        assert repr(pack) == f'<Pack {pack.name}>'

    def test_type_err(self, pack):
        with pytest.raises(TypeError):
            pack.add(8)


class TestPackMaker:
    def test_get_pack_list(self, path, file_json, pack_maker, pack_names, pack):
        assert isinstance(pack_maker.make_pack_list(path.file), list)
        assert isinstance(pack_maker.make_pack_list(file_json), list)
        packs = pack_maker.make_pack_list(path.file)
        assert all([isinstance(p, type(pack)) for p in packs])
        assert all([p.name in pack_names for p in packs])

    def test_add_list(self, path, pack_maker, add_list, pack_names):
        packs = pack_maker.make_pack_list(path.file, add_list=add_list)
        names = [pack.name for pack in packs]
        exclude_list = [name for name in pack_names if name not in names]
        assert all([name not in exclude_list and name in pack_names for name in names])

    def test_exc_list(self, path, pack_maker, exc_list, pack_names):
        packs = pack_maker.make_pack_list(path.file, exc_list=exc_list)
        names = [pack.name for pack in packs]
        assert all([name in pack_names and name not in exc_list for name in names])


class TestCfgParser:
    def test_parse(self, cfg_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in cfg_parser.parse(path.file)])

    def test__call__(self, cfg_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in cfg_parser(path.file)])

    def test_err(self, cfg_parser):
        assert cfg_parser.parse('bad_path') == []


class TestJsonParser:
    def test_parse(self, json_parser, file_json, pack_names):
        assert all([pack.name in pack_names for pack in json_parser.parse(file_json)])

    def test__call__(self, json_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in json_parser(path.file)])

    def test_error(self, json_parser, path):
        assert json_parser(path.file) == []


class TestParser:
    def test_parse(self, parser, path, pack_names):
        assert all([pack.name in pack_names for pack in parser.parse(path.file)])
        assert all([pack.name in pack_names for pack in parser.cfg(path.file)])
        assert all([pack.name in pack_names for pack in parser.cfg.parse(path.file)])
        assert all([pack.name in pack_names for pack in parser.json(path.file)])
        assert all([pack.name in pack_names for pack in parser.json.parse(path.file)])

    @pytest.mark.parametrize('suffix', ['.json', '.cfg'])
    def test__get_parser(self, parser, cfg_parser, json_parser, suffix):
        if suffix == '.json':
            assert isinstance(parser._get_parser(suffix), type(json_parser))
        else:
            assert isinstance(parser._get_parser(suffix), type(cfg_parser))

    def test__call__(self, parser, path, pack_names):
        assert all([pack.name in pack_names for pack in parser(path.file)])
