#!/usr/bin/python3
"""Cmd module for console project"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb) "
    variable_storage = ['BaseModel']

    def do_create(self, arg):
        """Creates an instance of the specified class"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.variable_storage:
            print("** class doesn't exist **")
            return

        new_instance = self.variable_storage[class_name]()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.variable_storage:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.variable_storage:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args[0], args[1]
        key = f"{class_name}.{obj_id}"


        if key in storage.all():
            del storage.all()[key]
            storage.save()
            return

        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(self, arg):
        """EOF Quits the program"""
        print()
        return True

    def emptyline(self):
        """Does nothing on empty line + enter"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
