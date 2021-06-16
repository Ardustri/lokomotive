import tests.path_config
from eternatus.cli import *


def test_answer():
    assert main() == 6
