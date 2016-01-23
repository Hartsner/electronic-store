from product import Product

class Software(Product):
    def __init__(self, name="unknown", manufacture="unknown", productnum=0, price=0.0, medium="unknown"):
        Product.__init__(self, name, manufacture, productnum, price)
        self.__medium = medium

    def __str__(self):
        return self.__name + self.__manufacture + self.__productnum + self.__price + self.__medium

    def set_medium(self, new_medium):
        self.__medium = new_medium
    def get_medium(self):
        return self.__medium