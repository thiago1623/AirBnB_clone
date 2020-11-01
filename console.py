#!/usr/bin/python3
"""
the console
"""
import cmd
import models
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

    #################
    # do command#
    #################

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

    #################
    # Help Functions#
    #################

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
