#!/usr/bin/python3
"""
the console
"""
import sys
import cmd


class HBNBCommand(cmd.Cmd):
    """Implementing cmd module that quits out of the interpreter when
    the user types quit or EOF.
    """
    intro = "---Welcome to hbnb! Type (?) or (help) to list commands.---"
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


    #################
   # Help Functions#
   #################

    def help_quit(self):
       """shows command help"""
       print("Quit command to exit the program")

    def help_EOF(self):
        """ shows command help"""
        print("CTRL + D (EOF) to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
