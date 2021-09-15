# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------


def filter_packs(packs, add_list=None, exc_list=None):
    add_list = [] if add_list is None else add_list
    exc_list = [] if exc_list is None else exc_list

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
    else:
        pack_list = [pack for pack in packs if pack.name in name_list]
    return pack_list
