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
        """Updates an instance"""
        try:
            arguments = inp.split()
            models.storage.reload()
            if len(arguments) == 0:
                print("** class name missing **")
                return False
            elif len(arguments) == 1:
                print("** instance id missing **")
                return False
            elif len(arguments) == 2:
                print("** attribute name missing **")
                return False
            elif len(arguments) == 3:
                print("** value missing **")
                return False
            if arguments[0] not in found_class:
                print("** class doesn't exist **")
            if arguments[0] in found_class:
                object = arguments[0] + "." + arguments[1]
                if object in models.storage.all():
                    to_update = models.storage.all()[object]
                    for keys in to_update.keys():
                        if keys == arguments[1]:
                            setattr(object[keys], arguments[2], arguments[3])
                            models.storage.save()
            else:
                print("** no instance found **")
        except Exception:
            raise

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
