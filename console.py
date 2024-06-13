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


class HBNBCommand(cmd.Cmd):
    """Console module"""
    prompt = "(hbnb) "
    variable_storage = {
            'BaseModel': BaseModel, 'User': User,
            'City': City, 'Place': Place,
            'Review': Review, 'Amenity': Amenity
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

    
    #def do_all(self, arg):
     #   """Prints all string representation
         # of all instances based or not on the class name"""
      #  args = shlex.split(arg)
       # all_instances = storage.all()
        #result = []

        #if len(args) == 0:
         #   for obj in all_instances.values():
          #      result.append(str(obj))

        #else:
         #   class_name = args[0]

          #  if class_name not in self.variable_storage:
           #     print("** class doesn't exist **")
            #    return

            # prints instances of the specified class
            #for obj in all_instances.values():
             #   if obj.__class__.__name__ == class_name:
              #      result.append(str(obj))

        #print(result)

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
        """Default if commands are not in class methods"""
        arg = args.split('.') #split the class_name(User) and method(all)

        #arg[0] = User
        #arg[1] = all()

        incoming_class = arg[0]
        #Now, arg[1] has all and ()
        #if we split using (, and ) we will have the method name
        incoming_method = arg[1].split('(')
        stated_method = incoming_method[0]

        possible_dict = {
                'all': self.do_all,
                'update': self.do_update,
                'destroy': self.do_destroy,
                'create': self.do_create,
                'count': self.do_count
                }
        if stated_method in possible_dict.keys():
            return possible_dict[stated_method](f"{incoming_class} {''}")
        print("Missing")
        return False


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
