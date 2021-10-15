# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestCfgParser:
    def test_parse_file(self, cfg_parser, path, pack_names):
        assert all([pack.name in pack_names for pack in cfg_parser.parse_file(path.file)])

    def test_return_type(self, path, cfg_parser):
        assert isinstance(cfg_parser(path.file), list)

    def test_error(self, cfg_parser):
        assert cfg_parser.parse_file('bad_path') == []


class TestJsonParser:
    def test_parse_file(self, json_parser, file_json, pack_names):
        assert all([pack.name in pack_names for pack in json_parser.parse_file(file_json)])

    def test_return_type(self, path, json_parser):
        assert isinstance(json_parser(path.file), list)

    def test_json_error(self, json_parser, path):
        assert json_parser(path.file) == []


class TestSmartParser:
    def test_parse_file(self, file_json, path, smart_parser, pack_names):
        packs1 = smart_parser(file_json)
        assert all([pack.name in pack_names for pack in packs1])
        packs2 = smart_parser(path.file)
        assert all([pack.name in pack_names for pack in packs2])

    def test_parse_cfg(self, path, smart_parser, pack_names):
        packs = smart_parser(path.file)
        assert all([pack.name in pack_names for pack in packs])

    def test_parse_json(self, file_json, smart_parser, pack_names):
        packs = smart_parser(file_json)
        assert all([pack.name in pack_names for pack in packs])


class TestParsersFactory:
    def test_get_cfg_parser(self, parsers_factory, cfg_parser):
        assert isinstance(parsers_factory.get_cfg_parser(), type(cfg_parser))

    def test_get_json_parser(self, parsers_factory, json_parser):
        assert isinstance(parsers_factory.get_json_parser(), type(json_parser))


def test_parse_cfg_file(parse_cfg_file, path, pack_names):
    assert all([pack.name in pack_names for pack in parse_cfg_file(path.file)])


def test_parse_json_file(parse_json_file, file_json, pack_names):
    assert all([pack.name in pack_names for pack in parse_json_file(file_json)])


def test_parse_packs(parse_packs, path, file_json, pack_names):
    assert all([pack.name in pack_names for pack in parse_packs(path.file)])
    assert all([pack.name in pack_names for pack in parse_packs(file_json)])
