#recurssion

# def python():
#     print('Python')
#     python()
# python()

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)

n=0

def python():
    global n
    n=n+1
    print('Python')
    python()
python()