#!/usr/bin/env python3

class Shoe:
#Shoe in shoe.py has the brand and size passed to __init__, and values can be set to new instance.  
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

#Shoe in shoe.py prints "size must be an integer" if size is not an integer
    def get_size(self):
        return self._size
    def set_size(self, size):
        if (isinstance(size, int)):
            self._size = size
        else:
            print("size must be an integer")
    size = property(get_size, set_size)

#Shoe in shoe.py says that the shoe has been repaired.
#Shoe in shoe.py creates an attribute on the instance called 'condition' and set equal to 'New' after repair.
    def cobble(self):
       self.condition = "New"
       print("Your shoe is as good as new!")