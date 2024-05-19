#!/usr/bin/python3
""" console model """
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb) "
    objects_list = [
        'BaseModel', 'State', 'City', 'User', 'Amenity', 'Place', 'Review'
    ]

    def precmd(self, line):
        """override precmd process"""
        do_separation = 0  # to ensure its in form class.method() or not
        for i in HBNBCommand.objects_list:
            if f"{i}." in line:
                do_separation = 1
                break
        if do_separation:
            l2, dot, l1 = line.partition('.')  # l1 -> method, l2->class name
            '''
             this is the first not efficient approch
            count = 0
            for char in l1:
                if char != '(':
                    count += 1
                else:
                    iid = l1[count + 2:-2]
                    return f"{l1[0:count]} {l2} {iid}"
            <class name>.update(<id>, <attribute name>, <attribute value>)
            l1=update 22222222 attr attrv
            '''
            l1 = l1.replace('(', '|')
            l1 = l1.replace(')', '')
            like = re.search(r'{.+}', l1)  # catch the dictionary befor " edit
            l1 = l1.replace('"', '')
            l1 = l1.replace(", ", "|")
            if like:
                l1 = re.sub(r'{.+}', '', l1)  # remove dict representation
            mth_list = l1.split('|')
            if l1.endswith('|'):
                del(mth_list[len(mth_list) - 1])
            for order, elem in enumerate(mth_list):  # to ensure no whitespaces
                mth_list[order] = elem.strip()
            mth_list.insert(1, l2)  # to insert class name
            if like:
                for k, v in eval(like.group()).items():
                    mth_list.insert(len(mth_list), k)  # add k in end
                    mth_list.insert(len(mth_list), v)  # add v in end
            return ' '.join(str(x) for x in mth_list)
        else:
            return line

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.objects_list:
            print("** class doesn't exist **")
        else:
            temp_list = line.split(" ")
            obj_dict = storage.all()
            cls_name = temp_list[0]
            inst = eval(cls_name)()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        temp_list = line.split(" ")
        obj_dict = storage.all()

        if not line:
            print("** class name missing **")
        elif temp_list[0] not in HBNBCommand.objects_list:
            print("** class doesn't exist **")
        elif len(temp_list) == 1:
            print("** instance id missing **")
        else:
            for key, value in obj_dict.items():
                cls_name, cls_id = key.split('.')
                if cls_id == temp_list[1] and cls_name == temp_list[0]:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        temp_list = line.split(" ")
        obj_dict = storage.all()

        if not line:
            print("** class name missing **")
        elif temp_list[0] not in HBNBCommand.objects_list:
            print("** class doesn't exist **")
        elif len(temp_list) == 1:
            print("** instance id missing **")
        else:
            for key in obj_dict.keys():
                cls_name, cls_id = key.split('.')
                if cls_id == temp_list[1]:
                    del(obj_dict[key])
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        temp_list = line.split(" ")
        obj_dict = storage.all()
        ret_list = []

        for k, v in obj_dict.items():
            if not line:
                ret_list.append(v.__str__())
            elif len(temp_list) == 1:
                if temp_list[0] not in HBNBCommand.objects_list:
                    print("** class doesn't exist **")
                    return
                else:
                    string, iid = k.split('.')
                    if k.startswith(temp_list[0]):
                        ret_list.append(v.__str__())
            else:
                pass
        print(ret_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        temp_list = line.split(" ")
        obj_dict = storage.all()

        if not line:
            print("** class name missing **")
        elif temp_list[0] not in HBNBCommand.objects_list:
            print("** class doesn't exist **")
        elif len(temp_list) == 1:
            print("** instance id missing **")
        elif len(temp_list) == 2:
            print("** attribute name missing **")
        elif len(temp_list) == 3:
            print("** value missing **")
        elif len(temp_list) >= 4 and len(temp_list) % 2 == 0:
            units = (len(temp_list) - 4) // 2  # units start from 0
            '''
            when updating more than 1 attribute, work logic:
                units ----> number of attributes to be updated 0 when 1 attr
                make a loop and units decreases by 1 after any update
                to locate attrs in temp_list:
                    units+2 , units+3
                    then multiply units by 2 for every update
                    to reach the next pair
                    units * 2 + 2 for attr
                    units * 2 + 3 for val
            '''
            for k, v in obj_dict.items():
                cls_name, cls_id = k.split('.')
                if cls_id == temp_list[1]:
                    while units >= 0:
                        setattr(v, temp_list[units * 2 + 2],
                                temp_list[units * 2 + 3])
                        units -= 1
                    storage.save()
                    return
            print("** no instance found **")

    def do_count(self, line):
        """ retrieve the number of class instances:<class name>.count()"""
        obj_dict = storage.all()
        count = 0
        for k in obj_dict.keys():
            if k.startswith(line):
                count += 1
        print(count)

    def do_EOF(self, line):
        """EXIT"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """print nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
