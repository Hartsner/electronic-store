

import pickle
class Product:
    def __init__(self, name="unknown", manufacture="unknown", productnum=0, price=0.0):
        self.__name = name
        self.__manufacture = manufacture
        self.__productnum = productnum
        self.__price = price

    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name

    def set_manufacture(self, new_manufacture):
        self.__manufacture = new_manufacture
    def get_manufacture(self):
        return self.__manufacture
    
    def set_productnum(self, new_productnum):
        self.__productnum = new_productnum
    def get_productnum(self):
        return self.__productnum

    def set_price(self, new_price):
        self.__price = new_price
    def get_price(self):
        return self.__price

    def print_format(self):
        template = "{0:15}|{1:15}|{2:15}|{3:15}"
        template.format(self.get_name(), self.get_manufacture(), self.get_productnum(), self.get_price())

class prod_list:
    def __init__(self):
        self.__prod_list = []

    def set_product_list(self, item_list):
        self.__prod_list.append(item_list)

    def get_product_list(self):
        return self.__prod_list

