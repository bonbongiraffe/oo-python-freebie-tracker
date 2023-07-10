
class Freebie:
    all = []

    def __init__( self, item_name, value, dev, company ):
        self.item_name = item_name
        self.value = value
        self.dev = dev
        self.company = company
        Freebie.all.append(self)

    def print_details( self ):
        print(f'{self.dev.name} owns a {self.item_name} from {self.company.name}')
    
    @property
    def item_name( self ):
        return self._item_name
    
    @item_name.setter
    def item_name( self, item_name ):
        if type(item_name) == str:
            self._item_name = item_name
        else:
            raise Exception("Item name must be string.")

    @property
    def value( self ):
        return self._value
    
    @value.setter
    def value( self, value):
        if type(value) == int:
            self._value = value
        else:
            raise Exception("Value must be an integer.")