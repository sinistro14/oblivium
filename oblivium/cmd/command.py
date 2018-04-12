#!/usr/bin/env python3.6

from cmd import Cmd


class Command(Cmd):

    def __init__(self):
        super().__init__()
        self._shell_name = "oblivium-" + self.shell_name()
        self.intro = "Welcome to " + self.shell_name()
        self.prompt = "(" + self.shell_name() + ") > "
        self.cmdloop('Starting prompt...')

    def shell_name(self):
        """Returns prompt name"""
        if self._shell_name is None:
            raise NotImplementedError("Attribute must be defined by subclass")
        return self._shell_name

    def do_exit(self, args):
        """Exists the program"""
        print("Exiting " + self.shell_name() + "...")
        raise SystemExit
