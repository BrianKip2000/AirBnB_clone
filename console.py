#!/usr/bin/python3
"""Cmd module for console project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates an instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance"""
        from models import storage
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            class_name, obj_id = args

            eval(class_name)

        except NameError:
            print("** class doesnt exist **")

        instance = storage.get(class_name, obj_id)
        if not instance:
            print("** no instance found **")
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        try:
            class_name, obj_id = args
            eval(class_name)
        except NameError:
            print("** class doesnt exist **")

        instance = storage.get(class_name, obj_id)
        if not instance:
            print("** no instance found **")
        else:
            storage.delete(instance)
            storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        print([str(obj) for obj in storage.all(args[0])])

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        instance = storage.get(args[0], args[1])
        if not instance:
            print("** no instance found **")
            return
        else:
            setattr(instance, args[2], args[3])
            instance.save()
       
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
