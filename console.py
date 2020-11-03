#!/usr/bin/python3
"""
the Airbnb console
"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.city import City
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
        return True

    def emptyline(self):
        """when line is empty do nothing"""
        pass

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

    def do_count(self, inp):
        """Method that counts the instance of a class
        """
        count = 0
        clas = inp.split()
        objs = models.storage.all()
        if not clas[0] in found_class:
            print("** class doesn't exist **")
            return None
        for key, value in objs.items():
            if value.__class__.__name__ == clas[0]:
                count += 1
        print(count)


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

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")

    ##########
    # call all function
    #########

    def do_User(self, args):
        """Usages:
        User.all() - displays all objects of class User
        User.count() - displays number of objects of class User
        User.show(<id>) - displays object of class User with id
        User.destroy(<id>) - deletes object of class User with id
        User.update(id, attribute name, attribute value) - update User
        User.update(<id>, <dictionary representation>) - update User
        """
        self.class_exec('User', args)

    def do_BaseModel(self, args):
        """Usages:
        BaseModel.all() - displays all objects of class BaseModel
        BaseModel.count() - displays number of objects of class BaseModel
        BaseModel.show(<id>) - displays object of class BaseModel with id
        BaseModel.destroy(<id>) - deletes object of class BaseModel with id
        BaseModel.update(id, attribute name, attribute value) - update
        BaseModel.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('BaseModel', args)

    def do_State(self, args):
        """Usages:
        State.all() - displays all objects of class State
        State.count() - displays number of objects of class State
        State.show(<id>) - displays object of class State with id
        State.destroy(<id>) - deletes object of class BaseModel with id
        State.update(<id>, <attribute name>, <attribute value>) - update
        State.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('State', args)

    def do_City(self, args):
        """Usages:
        City.all() - displays all objects of class City
        City.count() - displays number of objects of class City
        City.show(<id>) - displays object of class City with id
        City.destroy(<id>) - deletes object of class City with id
        City.update(<id>, <attribute name>, <attribute value>) - update
        City.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('City', args)

    def do_Amenity(self, args):
        """Usages:
        Amenity.all() - displays all objects of class Amenity
        Amenity.count() - displays number of objects of class Amenity
        Amenity.show(<id>) - displays object of class Amenity with id
        Amenity.destroy(<id>) - deletes object of class Amenity with id
        Amenity.update(<id>, <attribute name>, <attribute value>) - update
        Amenity.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Amenity', args)

    def do_Place(self, args):
        """Usages:
        Place.all() - displays all objects of class Place
        Place.count() - displays number of objects of class Place
        Place.show(<id>) - displays object of class Place with id
        Place.destroy(<id>) - deletes object of class Place with id
        Place.update(<id>, <attribute name>, <attribute value>) - update
        Place.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Place', args)

    def do_Review(self, args):
        """Usages:
        Review.all() - displays all objects of class Review
        Review.count() - displays number of objects of class Review
        Review.show(<id>) - displays object of class Review with id
        Review.destroy(<id>) - deletes object of class Review with id
        Review.update(<id>, <attribute name>, <attribute value>) - update
        Review.update(<id>, <dictionary representation>) - update
        """
        self.class_exec('Review', args)


    def class_exec(self, cls_name, args):
            """Wrapper function for <class name>.action()"""
            if args[:6] == '.all()':
                self.do_all(cls_name)
            elif args[:7] == '.count(':
                self.do_count(cls_name)
            elif args[:6] == '.show(':
                self.do_show(cls_name + ' ' + args[7:-2])
            elif args[:9] == '.destroy(':
                self.do_destroy(cls_name + ' ' + args[10:-2])
            elif args[:8] == '.update(':
                if '{' in args and '}' in args:
                    new_arg = args[8:-1].split('{')
                    new_arg[1] = '{' + new_arg[1]
                else:
                    new_arg = args[8:-1].split(',')
                if len(new_arg) == 3:
                    new_arg = " ".join(new_arg)
                    new_arg = new_arg.replace("\"", "")
                    new_arg = new_arg.replace("  ", " ")
                    self.do_update(cls_name + ' ' + new_arg)
                elif len(new_arg) == 2:
                    try:
                        dict = eval(new_arg[1])
                    except:
                        return
                    for j in dict.keys():
                        self.do_update(cls_name + ' ' + new_arg[0][1:-3] + ' '
                                       + str(j) + ' ' + str(dict[j]))
                else:
                    return
            else:
                print("Not a valid command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
