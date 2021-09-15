# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------
import pytest


class TestCommons:
    def test_filter_packs_dict(self, filter_packs, pack_dict, pack_names):
        packs = filter_packs(pack_dict)
        assert isinstance(packs, list)
        assert all([pack.name in pack_names for pack in packs])

    def test_filter_packs_dict_add_packs(self, filter_packs, pack_dict, pack_names):
        add_list = ['Ubuntu']
        packs = filter_packs(pack_dict, add_list=add_list)
        assert all([pack.name in add_list for pack in packs])

    def test_filter_packs_list(self, filter_packs, pack_list, pack_names):
        packs = filter_packs(pack_list)
        assert isinstance(packs, list)
        assert all([pack.name in pack_names for pack in packs])

    def test_filter_packs_list_add_packs(self, filter_packs, pack_list, pack_names):
        add_list = ['Ubuntu']
        packs = filter_packs(pack_list, add_list=add_list)
        assert all([pack.name in add_list for pack in packs])

    def test_type_error(self, filter_packs):
        with pytest.raises(TypeError):
            filter_packs(1)
