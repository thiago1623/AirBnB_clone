#!/usr/bin/python3
"""
the console
"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

found_class = {"Amenity": Amenity, "BaseModel": BaseModel, "Place": Place,
               "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    """
    intro = "---Welcome to hbnb console! Type (?) or (help)to list commands---"
    prompt = "(hbnb)"

    ###############
    # do command #
    ##############

    def do_quit(self, inp):
        """ command to exit the program"""
        return True

    def do_EOF(self, inp):
        """ command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """when line is empty do nothing"""
        return False

    def do_create(self, inp):
        """command to create an new instance"""
        try:
            arguments = inp.split()
            if len(arguments) == 0:
                print("** class name missing **")
                return False
            if arguments[0] in found_class:
                object = found_class[arguments[0]]()
            else:
                print("** class doesn't exist **")
                return False
            print(object.id)
            object.save()
        except Exception:
            raise

    def do_show(self, inp):
        """ show """
        try:
            arguments = inp.split()
            models.storage.reload()
            if (len(arguments) == 0):
                print("** class name missing **")
                return False
            if arguments[0] in found_class:
                if(len(arguments) > 1):
                    object = arguments[0] + "." + arguments[1]
                    if object in models.storage.all():
                        '''dynamic instance'''
                        print(models.storage.all()[object])
                elif (len(arguments) == 1):
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except Exception:
            raise

    def do_all(self, inp):
        """ show all"""
        try:
            arguments = inp.split()
            models.storage.reload()
            empty_list = []
            if arguments[0] in found_class:
                object = arguments[0]
                for object in models.storage.all():
                    empty_list.append(str(models.storage.all()[object]))
                print("[", end='')
                print(",".join(empty_list), end="")
                print("]")
            else:
                print("** class doesn't exist **")
        except Exception:
            raise

    def do_destroy(self, inp):
        """ Destroy instance"""
        try:
            arguments = inp.split()
            models.storage.reload()
            if (len(arguments) == 0):
                print("** class name missing **")
                return False
            if arguments[0] in found_class:
                if (len(arguments) > 1):
                    object = arguments[0] + "." + arguments[1]
                    models.storage.all().pop(object)
                    models.storage.save()
                elif len(arguments) == 1:

                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except Exception:
            raise

    def do_update(self, inp):
        """ update an instance based on its UUID """
        models.storage.reload()
        if len(inp) == 0:
            print("** class name missing **")
            return
        else:
            arguments = shlex.split(inp)
            if arguments[0] not in found_class:
                print("** class doesn't exist **")
                return
            if arguments[0] in found_class and len(arguments) < 2:
                print("** instance id missing **")
                return
            object = arguments[0] + '.' + arguments[1]
            if object in models.storage.all():
                to_update = models.storage.all()[object].__dict__
                if len(arguments) < 3:
                    print("** attribute name missing **")
                elif len(arguments) < 4:
                    print("** value missing **")
                else:
                    key = arguments[2]
                    try:
                        attr = type(to_update[key])
                        value = attr(arguments[3])
                    except KeyError:
                        value = arguments[3]
                    to_update[key] = value
                    models.storage.save()
            else:
                print("** no instance found **")

    ##################
    # Help Functions #
    ##################

    def help_quit(self):
        """shows command help"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """ shows command help"""
        print("CTRL + D (EOF) to exit the program")

    def help_create(self):
        print("Usage: create <valid class name>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
