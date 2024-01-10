# CHARACTERS AND CHARACTER SEQUENCES

# ^ - Matches the beginning of a line ^I
# $ - Matches the end of a line   g$
# . - Matches any character ^I
# \d - Matches any digit 
# \D - Matches any non- digit
# \s - Matches whitespace
# \s-Matches any non- whitespace

import re
string='It is a dog 56'
pattern ='\S'
print(re.findall(pattern,string,flags=0))


