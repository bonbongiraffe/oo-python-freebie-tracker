from .freebie import Freebie

class Dev:
    def __init__( self, name ):
        self.name = name

    def freebies( self ):
        return [x for x in Freebie.all if x.dev == self]

    def companies( self ):
        company_list = []
        for freebie in self.freebies():
            if freebie.company not in company_list:
                company_list.append(freebie.company)
        return company_list

    def received_one( self, item_name ):
        for freebie in self.freebies():
            if freebie.item_name == item_name:
                return True
        return False

    def give_away( self, dev, freebie ):
        if freebie.dev == self:
            freebie.dev = dev
        else:
            raise Exception(f"Freebie does not belong to {self.name}!")
    
    @property
    def name( self ):
        return self._name
    
    @name.setter
    def name( self, name ):
        if type(name) == str:
            self._name = name
        else:
            raise Exception("name must be a string.")