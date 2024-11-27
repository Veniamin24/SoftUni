class Inventory:


    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []


    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return 'not enough room in the inventory'


    def get_capacity(self):
        return self.__capacity


    def __repr__(self):
        items = ', '.join(self.items)
        return f"Items: {items}.\nCapacity left: {self.__capacity - len(self.items)}"
