from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # access all attributes from inherited class
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones{broken_phones} not grater than or equal to Zero"

        # assign
        self.broken_phones = broken_phones