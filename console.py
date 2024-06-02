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

    def default(self, arg):
        """Default behavior for cmd"""
        args = arg.split('.')
        if len(args) == 1:
            cmd = args[0]
            if cmd == 'all()':
                self.do_all()
            elif cmd == 'count()':
                print(len(storage.all()))
            elif cmd == 'show()':
                print("** instance id missing **")
            elif cmd == 'destroy()':
                print("** instance id missing **")
            elif cmd == 'update()':
                print("** instance id missing **")
            elif cmd == 'update()':
                print("** attribute name missing **")
            elif cmd == 'update()':
                print("** value missing **")
            else:
                print("*** Unknown syntax: {}".format(arg))
        elif len(args) == 2:
            cmd = args[0] + ' ' + args[1]
            if cmd == 'all()':
                self.do_all(args[0])
            elif cmd == 'count()':
                self.do_count(args[0])
            elif cmd == 'show()':
                self.do_show(args[0] + ' ' + args[1])
            elif cmd == 'destroy()':
                self.do_destroy(args[0] + ' ' + args[1])
            elif cmd == 'update()':
                self.do_update(args[0] + ' ' + args[1])
            elif cmd == 'update()':
                self.do_update(args[0] + ' ' + args[1] + ' ' + args[2])
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("*** Unknown syntax: {}".format(arg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
