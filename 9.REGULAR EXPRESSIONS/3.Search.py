#Search (Patter, strings, flags)

import re
pattern='Debraj'
if re.search(pattern,'checkheeDebraj',flags = 0):
    print('True')
else:
    print('False')
    
import re
pattern='Debraj'
if re.match(pattern,'Debrajgje',flags = 0):
    print('True')
else:
    print('False')
