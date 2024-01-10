#Match ( Patter , string Flags)

# import re

# pattern='Mango'
# if re.match(pattern,'Mang0',flags=0):
#     print("Pattern found at the start of the String")
# else:
#     print("Pattern not found at the start of the String")


#findall( Parrtern , string flags)
import re
pattern = 'Apple'
string = re.findall('App',pattern)
print(string)



