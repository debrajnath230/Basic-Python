import re

string ='babac'
pattern ='a'

# if re.match(pattern,string):
#     print('Match Found')
# else:
#     print('match not found')
    
if re.search(pattern,string):
    print('Match Found')
else:
    print('match not found')