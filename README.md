# commandpack

***

I recommend using my new library [commandex](https://github.com/smartlegionlab/commandex). 

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/commandpack)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/commandpack?label=pypi%20downloads)](https://pypi.org/project/commandpack/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/commandpack)](https://github.com/smartlegionlab/commandpack/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/commandpack)](https://github.com/smartlegionlab/commandpack/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/commandpack)](https://pypi.org/project/commandpack)
[![PyPI - Format](https://img.shields.io/pypi/format/commandpack)](https://pypi.org/project/commandpack)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/commandpack?style=social)](https://github.com/smartlegionlab/commandpack/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/commandpack?style=social)](https://github.com/smartlegionlab/commandpack/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/commandpack?style=social)](https://github.com/smartlegionlab/commandpack/)

***

## Help the project financially:

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Short Description:

___commandpack___ -  A cross-platform library for creation, storage, management of commands and command packages. Execution of commands, parsing of files with command packages.

***

Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## Requirements:

- [Python](https://python.org) 3.6+
  - [Download](https://python.org)
  
***

## What's new?

___commandpack v0.2.0___

- The 0.2.x versions will not be backward compatible with older versions, since the code is completely
revised and improved. Bugs fixed. New more convenient tools have been added.

- If you have problems, use version 0.1.x

- Documentation will be added in future versions.

***

## Description:

A cross-platform library for creation, storage, management of commands and command packages. 
Execution of commands, parsing of files with command packages.
 
Used to create utilities for working with commands (execution, launch, autorun, storage).

You can keep your commands in simple and understandable files, collect them in one place,
split into named categories (packages) and execute at any time:

The files must have the extension *.cfg, or *.json and have the correct structure:


### commands.cfg:

```text
[package name 1]
command 1
command 2
command N

[package name 2]
command 1
command 2
command N
```

### commands.json:

```json5
{
  "name1":

  [
    "command1",
    "command2",
    "commandN"
  ],

  "name2":

  [
    "command1",
    "command2",
    "commandN"
  ]
}
```

***


## Help:

### Install and Use:

- `pip3 install commandpack`

Available tools:

- Command executors
- Pack makers
- Parsers
- Commands
- Packs
- Factories

```python
from commandpack.factories import Factory

os_executor = Factory.tools.get_os_executor()
sub_executor = Factory.tools.get_sub_executor()
executor = Factory.tools.get_executor()

command = Factory.tools.command_pack.create_command('pip list')
pack = Factory.tools.command_pack.create_pack('default')

cfg_parser = Factory.tools.parsers.get_cfg_parser()
json_parser = Factory.tools.parsers.get_json_parser()
parser = Factory.tools.parsers.get_parser()

pack_maker = Factory.tools.makers.get_pack_maker()

```

### Termux support:

Utilities created with use work "commandpack", without problems in Termux.

### Windows support:

- Install [python](https://python.org)
- `pip3 install commandpack`

Utilities created with use work "commandpack", without problems in Windows:

### Test coverage:

#### Run tests:
- `pip3 install pytest`
- `pytest -v`
  

#### __Test coverage 100%__

- `pip install pytest-coverage`
- `pytest --cov`

![commandpack image](https://github.com/smartlegionlab/commandpack/raw/master/data/images/commandpack.png)


#### Report html:

- `pytest --cov --cov-report=html`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
