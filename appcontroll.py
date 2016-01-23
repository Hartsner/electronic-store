# coding: utf-8
from view import UI
from hardware import Hardware
from software import Software
from product import *


class AppController:
    def __init__(self):
        self.__ui = UI()
        self.__list = prod_list()

    def run(self):
        choice = -1
        while choice != 0:
            self.__ui.show_menu()
            choice = self.__ui.get_menu_choice()
            if choice == 1:
                choice2 = self.__ui.product_menu()
                if choice2 == 1:
                   self.new_hardware()
                if choice2 == 2:
                    self.new_software()
                elif choice2 == 0:
                    self.__ui.show_menu()
            if choice == 2:
                self.show_prod()
            elif choice == 3:
                self.single_item()

    
    #lagger till product
    def new_hardware(self):
        while True:
            name = raw_input("vilket namn? ")
            if name == "":
                print("Invalid input.")
            else:
                break
        while True:
            manufacture = raw_input("Vilken tillverkare? ")
            if manufacture == "":
                print("Invalid input.")
            else:
                break
        while True:
            try:
                productnum = int(raw_input("Vilket produktnummer? "))
                break
            except ValueError:
                print("Invalid input.")
        while True:
            try:
                price = float(raw_input("Vilket pris? "))
                break
            except ValueError:
                print("Invalid input.")
        while True:
            try:
                weight = float(raw_input("Vikt i kg? "))
                if weight >= 25:
                    price = price + 200
            except ValueError:
                print("Invalid input")
            else:
                break
        hw = Hardware(name, manufacture, productnum, price, weight)
        self.__list.set_product_list(hw)
        

    def new_software(self):
        while True:
            name = raw_input("vilket namn? ")
            if name == "":
                print("Invalid input.")
            else:
                break
        while True:
            manufacture = raw_input("Vilken tillverkare? ")
            if manufacture == "":
                print("Invalid input.")
            else:
                break
        while True:
            try:
                productnum = int(raw_input("Vilket produktnummer? "))
                break
            except ValueError:
                print("Invalid input.")
        while True:
            try:
                price = float(raw_input("Vilket pris? "))
                break
            except ValueError:
                print("Invalid input.")
        while True:
            medium = str(raw_input("DVD/CD? "))
            if medium == "DVD":
                break
            elif medium == "CD":
                break
            else:
                print("Invalid input.")
        sw = Software(name, manufacture, productnum, price, medium)
        self.__list.set_product_list(sw)
        
    """printar ut produkter"""
    def show_prod(self):
        template = "{0:15}|{1:15}|{2:15}"
        print template.format("Namn", "Produktnr", "Pris")
        for i in self.__list.get_product_list():
            print template.format(i.get_name(), i.get_productnum(), i.get_price())

    """skapar produkter som laddas uppe i abc()"""
    def abc(self):
        h1 = Hardware("Skrivare", "HP", 1, 500.00, 25)
        self.__list.set_product_list(h1)
        h2 = Hardware("Scanner", "WD", 2, 100.00, 25)
        self.__list.set_product_list(h2)
        s1 = Software("Office", "Microsoft", 3, 999.00, "DVD")
        self.__list.set_product_list(s1)

    """Användaren ska kunna välja en specifik produkt genom någon typ av index"""
    def single_item(self):
        template = "{0:15}|{1:15}|{2:15}|{3:15}"
        num = int(raw_input("Enter productnumber: "))
        found = None
        for prod in self.__list.get_product_list():
            if prod.get_productnum() == num:
                found = prod
        if found:
            print template.format("Namn", "Tillverkare", "Produktnr", "Pris")
            print template.format(found.get_name(), found.get_manufacture(), found.get_productnum(), found.get_price())
            #found.print_format()
        else:
            print "Det finns ingen sådan produkt"