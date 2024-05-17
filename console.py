#!/usr/bin/python3
""" console model """
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = "(hbnb) "
    objects_list = [
        'BaseModel', 'State', 'City', 'User', 'Amenity', 'Place', 'Review'
    ]

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            inst = BaseModel()
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
        elif temp_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(temp_list) == 1:
            print("** instance id missing **")
        else:
            for key, value in obj_dict.items():
                if key == f"BaseModel.{temp_list[1]}":
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
        elif temp_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(temp_list) == 1:
            print("** instance id missing **")
        else:
            for key in obj_dict.keys():
                if key == f"BaseModel.{temp_list[1]}":
                    del(obj_dict[f'BaseModel.{temp_list[1]}'])
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
        elif temp_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(temp_list) == 1:
            print("** instance id missing **")
        elif len(temp_list) == 2:
            print("** attribute name missing **")
        elif len(temp_list) == 3:
            print("** value missing **")
        elif len(temp_list) < 5:
            for key, value in obj_dict.items():
                cls_name, cls_id = key.split('.')
                if cls_id == temp_list[1]:
                    setattr(value, temp_list[2], temp_list[3])
                    storage.save()
                    return
            print("** no instance found **")

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
