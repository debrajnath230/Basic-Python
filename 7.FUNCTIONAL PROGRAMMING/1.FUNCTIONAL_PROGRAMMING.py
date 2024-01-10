# def add(i,j):
#     return i+j
# a=add
# result = a(1,2)
# print(result)

def add(i,j):
    return i+j

def call(i,j):
    return add(i,j)

def pas(i,j,fn):
    return fn(i,j)
    
# result = a(1,2)
# print(result)

res =pas(1,2,call)
print(res)

