# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from commandpack.parsers import parse_packs


class PackMaker:

    @classmethod
    def get_pack_list(cls, file, add_list=None, exc_list=None):
        add_list = [] if add_list is None else add_list
        exc_list = [] if exc_list is None else exc_list
        packs = parse_packs(file=file)
        kwargs = dict(packs=packs, add_list=add_list, exc_list=exc_list)
        pack_list = cls.filter_pack_list(**kwargs)
        return pack_list

    @classmethod
    def filter_pack_list(cls, packs, add_list=None, exc_list=None):
        if isinstance(packs, dict):
            names = packs.keys()
        elif isinstance(packs, list):
            names = [pack.name for pack in packs]
        else:
            raise TypeError
        if add_list:
            name_list = [name for name in add_list if name in names and name not in exc_list]
        else:
            name_list = [name for name in names if name in names and name not in exc_list]
        if isinstance(packs, dict):
            pack_list = [pack for pack in packs.values() if pack.name in name_list]
        elif isinstance(packs, list):
            pack_list = [pack for pack in packs if pack.name in name_list]
        else:
            raise TypeError
        return pack_list


def make_pack_list(file, add_list=None, exc_list=None):
    add_list = [] if add_list is None else add_list
    exc_list = [] if exc_list is None else exc_list
    return PackMaker.get_pack_list(file=file, add_list=add_list, exc_list=exc_list)
