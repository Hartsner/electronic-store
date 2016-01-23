# coding: utf-8
class UI:
    def show_menu(self):
        print """
        1. Add product
        2. Show all products
        3. Show one product
        0. Exit
        """

    def product_menu(self):
        return input("""
        1. Add hardware
        2. Add software 
        0. Return

        Välj produkt: """)

    def get_menu_choice(self):
        return input("What do you want to do? ")
    


