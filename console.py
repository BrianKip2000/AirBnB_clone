#!/usr/bin/python3
"""Cmd module for console project"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import models
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb) "
    variable_storage = {
            'BaseModel': BaseModel, 'User': User,
            'City': City, 'Place': Place,
            'Review': Review, 'Amenity': Amenity,
            'State': State
            }

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
        new_instance.save()
        print(new_instance.id)

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

    def do_all(self, arg):
        """Prints all string representation of all instances of a given class"""
        args = shlex.split(arg)
        all_instances = storage.all()
        result = []

        if len(args) == 0:
            for obj in all_instances.values():
                result.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in self.variable_storage:
                print("** class doesn't exist **")
                return
            # Retrieve all instances of the specified class using <class name>.all()
            result = [str(obj) for obj in all_instances.values() if obj.__class__.__name__ == class_name]

            print(result)

    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        tokensU = shlex.split(argument)

        if len(tokensU) == 0:
            print("** class name missing **")
            return

        elif len(tokensU) == 1:
            print("** instance id missing **")
            return

        elif len(tokensU) == 2:
            print("** attribute name missing **")
            return

        elif len(tokensU) == 3:
            print("** value missing **")
            return

        elif tokensU[0] not in self.variable_storage:
            print("** class doesn't exist **")
            return

        keyI = tokensU[0] + "." + tokensU[1]
        dicI = models.storage.all()

        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return

        try:
            typeA = type(getattr(instanceU, tokensU[2]))
            tokensU[3] = typeA(tokensU[3])
        except AttributeError:
            pass

        setattr(instanceU, tokensU[2], tokensU[3])
        models.storage.save()

    def do_count(self, arg):
        """Counts the number of instances of a given class"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.variable_storage:
            print("** class doesn't exist **")
            return

        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == class_name)
        print(count)

    def default(self, args):
        """Default method if commands are not in class methods"""
        arg = args.split('.')

        if len(arg) < 2:
            print("** invalid command **")
            return

        class_name = arg[0]
        method_call = arg[1]

        if class_name not in self.variable_storage:
            print("** class doesn't exist **")
            return

        method_args = method_call.split('(')
        method_name = method_args[0]

        if method_name == "show":
            if len(method_args) > 1:
                instance_id = method_args[1].rstrip(')')
                self.do_show(f"{class_name} {instance_id}")
            else:
                print("** instance id missing **")
        elif method_name == "destroy":
            if len(method_args) > 1:
                instance_id = method_args[1].rstrip(')')
                self.do_destroy(f"{class_name} {instance_id}")
            else:
                print("** instance id missing **")
        elif method_name == "update":
            if len(method_args) > 1:
                update_args = method_args[1].rstrip(')')
                
                # Check if update_args contains ',' to distinguish between dictionary and attribute update
                if ',' in update_args:
                    try:
                        instance_id, json_dict = update_args.split(',', 1)
                        json_dict = json_dict.strip()
                        if not (json_dict.startswith('{') and json_dict.endswith('}')):
                            print("** invalid dictionary representation **")
                            return
                        dictionary = eval(json_dict)  # Safely evaluate JSON-like string to dictionary
                        self.do_update(f"{class_name} {instance_id} {dictionary}")
                    except ValueError:
                        print("** invalid format **")

                else:
                    # Assume it's an attribute update with attribute name and value
                    try:
                        instance_id, attribute_name, attribute_value = update_args.split(',', 2)
                        attribute_name = attribute_name.strip()
                        
                        # Check if attribute_value is quoted and strip the quotes
                        if (attribute_value.startswith('"') and attribute_value.endswith('"')) or \
                                (attribute_value.startswith("'") and attribute_value.endswith("'")):
                            attribute_value = attribute_value[1:-1].strip()

                        self.do_update(f"{class_name} {instance_id} {attribute_name} '{attribute_value}'")
                    except ValueError:
                        print("** invalid format **")

            else:
                print("** instance id and update data missing **")

        else:
            possible_dict = {
                    'all': self.do_all,
                    'update': self.do_update,
                    'destroy': self.do_destroy,
                    'create': self.do_create,
                    'count': self.do_count,
                    }

            if method_name in possible_dict:
                if len(method_args) > 1:
                    cmd_args = method_args[1].rstrip(')')
                    if cmd_args:
                        cmd_args = f"{class_name} {cmd_args}"
                    else:
                        cmd_args = class_name
                else:
                    cmd_args = class_name
                possible_dict[method_name](cmd_args)
            else:
                print("** unknown command **")

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
