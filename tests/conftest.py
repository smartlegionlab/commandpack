import pytest

from commandpack.commandpack import Command
from commandpack.executors import OsCommandExecutor, SubCommandExecutor


@pytest.fixture(scope='session', name='command')
def get_command():
    return Command('echo "test"')


@pytest.fixture(name='command_name')
def get_command_title():
    return 'echo "test"'


@pytest.fixture(name='os_executor')
def os_executor():
    return OsCommandExecutor()


@pytest.fixture(name='sub_executor')
def sub_executor():
    return SubCommandExecutor()
