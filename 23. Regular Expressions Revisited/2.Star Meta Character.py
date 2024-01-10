import re

string ='abbc'
pattern ='ab*c'

if re.match(pattern,string):
    print('Match Found')
else:
    print('match not found')