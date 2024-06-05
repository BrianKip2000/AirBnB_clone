#!/usr/bin/python3
"""Cmd module for console project"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb) "
    variable_storage = {'BaseModel': BaseModel}

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

    def do_all(self, arg):
        """Prints all string representation
          of all instances based or not on the class name"""
        args = shlex.split(arg)
        all_instances = storage.all()
        result = []

        if len(args) == 0:
            for obj in all_instances.values():
                result.append(str(obj))

        else:
            class_name = args[0]

            if class_name not in self.variable_storage:
                print("** class does't exist **")
                return

            # prints instances of the specified class
            for obj in all_instances.values():
                if obj.__class__.__name__ == class_name:
                    result.append(str(obj))

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

# #!/usr/bin/python3
# """Cmd module for console project"""
# import cmd
# import shlex
# from models.base_model import BaseModel
# from models import storage


# class HBNBCommand(cmd.Cmd):
#     """Console module"""
#     prompt = "(hbnb) "
#     variable_storage = {'BaseModel': BaseModel}

#     def do_create(self, arg):
#         """Creates an instance of the specified class"""
#         args = shlex.split(arg)
#         if len(args) == 0:
#             print("** class name missing **")
#             return

#         class_name = args[0]
#         if class_name not in self.variable_storage:
#             print("** class doesn't exist **")
#             return

#         new_instance = self.variable_storage[class_name]()
#         print(new_instance.id)
#         new_instance.save()

#     def do_show(self, arg):
#         """Prints string representation of an instance"""
#         args = shlex.split(arg)
#         if len(args) == 0:
#             print("** class name missing **")
#             return

#         class_name = args[0]

#         if class_name not in self.variable_storage:
#             print("** class doesn't exist **")
#             return

#         if len(args) < 2:
#             print("** instance id missing **")
#             return

#         obj_id = args[1]
#         key = f"{class_name}.{obj_id}"

#         if key not in storage.all():
#             print("** no instance found **")
#             return

#         print(storage.all()[key])

#     def do_destroy(self, arg):
#         """Deletes an instance"""
#         args = shlex.split(arg)
#         if len(args) == 0:
#             print("** class name missing **")
#             return

#         class_name = args[0]

#         if class_name not in self.variable_storage:
#             print("** class doesn't exist **")
#             return

#         if len(args) < 2:
#             print("** instance id missing **")
#             return

#         class_name, obj_id = args[0], args[1]
#         key = f"{class_name}.{obj_id}"


#         if key in storage.all():
#             del storage.all()[key]
#             storage.save()
#             return

#         else:
#             print("** no instance found **")

#     def do_all(self, arg):
#         """Prints all string representation
#           of all instances based or not on the class name"""
#         args = shlex.split(arg)
#         all_instances = storage.all()
#         result = []

#         if len(args) == 0:
#             for obj in all_instances.values():
#                 result.append(str(obj))

#         else:
#             class_name = args[0]

#             if class_name not in self.variable_storage:
#                 print("** class does't exist **")
#                 return

#             # prints instances of the specified class
#             for obj in all_instances.values():
#                 if obj.__class__.__name__ == class_name:
#                     result.append(str(obj))

#         print(result)

#     def do_update(self, arg):
#         """Updates instance based on name and id"""
#         args = shlex.split(arg)

#         if len(args) == 0:
#             print("** class name missing **")
#             return
        
#         class_name = args[0]
#         if class_name not in self.variable_storage:
#             print("** class name doesn't exist **")
#             return

#         if len(args) < 2:
#             # checks that the id exists
#             print("** instance id missing **")
#             return
        
#         obj_id = arg[1]
#         all_objs = storage.all()
#         key = f"{class_name}.{obj_id}"

        
#         if key not in all_objs:
#             print(" ** no instance found **")
#             # return
        
#         obj = all_objs[key]

#         if len(args) < 3:
#             print("** attribute name missing **")
#             return
#         attr_name = args[2]
#         if len(args) < 4:
#             print("** value missing **")
#             return
        
#         attr_value = args[3]

#         # lets cast the attr value to correct type
#         attr_type = type(getattr(obj, attr_name))
#         if attr_type == int:
#             attr_value = int(attr_value)
#         elif attr_type == float:
#             attr_value = float(attr_value)
        
#         # Lets now update the attribute
#         setattr(obj, attr_name, attr_value)
#         obj.save()
#     # def do_update(self, arg):
#     #     """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
#     #     args = shlex.split(arg)

#     #     if len(args) == 0:
#     #         print("** class name missing **")
#     #         return

#     #     class_name = args[0]
#     #     if class_name not in self.variable_storage:
#     #         print("** class doesn't exist **")
#     #         return

#     #     if len(args) < 2:
#     #         print("** instance id missing **")
#     #         return

#     #     obj_id = args[1]
#     #     key = f"{class_name}.{obj_id}"

#     #     all_instances = storage.all()
#     #     if key not in all_instances:
#     #         print("** no instance found **")
#     #         return

#     #     if len(args) < 3:
#     #         print("** attribute name missing **")
#     #         return

#     #     attribute_name = args[2]

#     #     if len(args) < 4:
#     #         print("** value missing **")
#     #         return

#     #     attribute_value_str = args[3]

#     #     # Handling quoted string arguments
#     #     if attribute_value_str.startswith('"') and attribute_value_str.endswith('"'):
#     #         attribute_value_str = attribute_value_str[1:-1]

#     #     instance = all_instances[key]

#     #     # Ensure id, created_at, and updated_at are not updated
#     #     if attribute_name in ['id', 'created_at', 'updated_at']:
#     #         print("** can't update id, created_at, or updated_at **")
#     #         return

#     #     # Get the class of the instance
#     #     instance_class = type(instance)

#     #     # Get the attribute type
#     #     attribute_type = getattr(instance_class, attribute_name, None)

#     #     if attribute_type is None:
#     #         print("** attribute name doesn't exist **")
#     #         return

#     #     # Cast the attribute value to the correct type
#     #     try:
#     #         attribute_value = attribute_type(attribute_value_str)
#     #     except ValueError:
#     #         print("** invalid value type **")
#     #         return

#     #     # Update the attribute
#     #     setattr(instance, attribute_name, attribute_value)
#     #     instance.save()
#     #     print(instance)


#     def do_quit(self, arg):
#         """Quits the program"""
#         return True

#     def do_EOF(self, arg):
#         """EOF Quits the program"""
#         print()
#         return True

#     def emptyline(self):
#         """Does nothing on empty line + enter"""
#         pass

# if __name__ == '__main__':
#     HBNBCommand().cmdloop()

