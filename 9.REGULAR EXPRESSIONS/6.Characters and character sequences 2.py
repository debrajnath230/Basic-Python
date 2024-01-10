# CHARACTERS AND CHARACTER SEQUENCES
# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where string extraction is to start
# ) - Indicates where string extraction is to end
# ? - Matches the expression © to 1 times

import re
string = 'From debraj@gmail.com'
pattern='^From (\S+@\S+)'
print(re.findall(pattern,string,flags=0))