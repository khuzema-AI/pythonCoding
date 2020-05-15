from _pydecimal import *

a = Decimal('.10')
b = Decimal('.60')

x= a+a+a-b
print (f"x is {x}")
print (type(x))
