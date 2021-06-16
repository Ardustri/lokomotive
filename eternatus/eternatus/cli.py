import sys


def command_arg(index):
    try:
        return sys.argv[index]
    except IndexError:
        return False


command_name = command_arg(1)
command_args = command_arg(2)
command_opts = command_arg(3)

command = {
    "command_name": command_name,
    "command_args": command_args,
    "command_opts": command_opts
}


def main():
    return 6
