#!/usr/bin/python3
"""Cmd module for console project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb) "
    variable_storage = ["BaseModel"]

    def do_create(self, arg):
        """Creates an instance of BaseModel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split(" ")

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.variable_storage:
            print("** class doesn't exist **")            
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = f"{args[0]}.{args[1]}"
            
            if key not in storage.all():
                print("** no instance found **")
                return
        
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = arg.split(" ")

        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in self.variable_storage:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_id = args[1]
            key = f"{self.variable_storage}.{obj_id}"

            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception:
            print("error")
            return

    def do_quit(self):
        """Quits the program"""
        return True

    def do_EOF(self):
        """EOF Quits the program"""
        print()
        return True

    def emptyline(self):
        """Does nothing on empty line + enter"""
        pass
