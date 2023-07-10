import ipdb
from lib import *

#code here
c1 = Company("Apple",1900)
c2 = Company("Microsoft", 2000)
d1 = Dev("Adam")
d2 = Dev("Emiley")
f1 = Freebie("apple stuff", 100, d1, c1)
f2 = Freebie("microsoft stuff", 100, d2, c2)
f3 = Freebie("more apple stuff", 100, d2, c1)

ipdb.set_trace()