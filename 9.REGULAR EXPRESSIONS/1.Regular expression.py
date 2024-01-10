#regular Expressions
#regex
#strings
# Import Re
#Validate the input

# 1 Match Function
import re

pattern= 'Apple'

if re.match(pattern,'Appleball'):
    print('True')
else:
    print('False')