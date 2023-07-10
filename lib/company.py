from .freebie import Freebie

class Company:
    all = []

    def __init__( self, name, founding_year ):
        self.name = name
        self.founding_year = founding_year
        Company.all.append(self)

    def freebies( self ):
        return [x for x in Freebie.all if x.company == self]
    
    def devs( self ):
        devs_list = []
        for freebie in self.freebies():
            if freebie.dev not in devs_list:
                devs_list.append(freebie.dev)
        return devs_list
    
    def give_freebie(self, dev, item_name, value): 
        return Freebie(item_name, value, dev, self)

    @classmethod
    def oldest_company(cls):
        oldest_year = float("inf")
        winner = None
        for company in cls.all:
            if company.founding_year < oldest_company:
                winner = company
                oldest_year = company.founding_year
        return winner

    @property
    def name( self ):
        return self._name
    
    @name.setter
    def name( self, name ):
        if type(name) == str:
            self._name = name
        else:
            raise Exception("name must be string.")
    
    @property
    def founding_year( self ):
        return self._founding_year 

    @founding_year.setter
    def founding_year( self, founding_year ):
        if type(founding_year) == int:
            self._founding_year = founding_year
        else:
            raise Exception("founding year must be integer.")