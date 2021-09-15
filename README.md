# commandpack

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

## Short Description:

___commandpack___ -  A package of modules for working with commands, command packages, files with command packages.

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

### ___commandpack v0.1.1___

***

## Description:

A package of modules for working with commands, 
command packages, files containing command packages.
 
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
  "pack name":

  [
    "command1",
    "command2",
    "commandN"
  ],

  "pack name2":

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

![commandman image](https://github.com/smartlegionlab/commandpack/raw/master/data/images/commandpack.png)


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
