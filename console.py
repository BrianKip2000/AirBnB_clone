#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(self):
        """EOF Quits the program"""
        print()
        return True

    def emptyline(self):
        """Does nothing on empty line + enter"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
