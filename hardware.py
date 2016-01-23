from product import Product
class Hardware(Product):
    def __init__(self, name="unknown", manufacture="unknown", productnum=0, price=0.0, weight=0.0):
        Product.__init__(self, name, manufacture, productnum, price)
        self.__weight = weight

    def __str__(self):
        return self.__name + self.__manufacture + self.__productnum + self.__price + self.__weight 
        
    def set_weight(self, new_weight):
        self.__weight = new_weight
    def get_weight(self):
        return self.__weight
