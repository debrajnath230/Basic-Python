#map
#map( function ,ilterable)

def squar(a):
    return a%2 ==0

numbers=[1,2,3,4,5,6]
ans =list(map(squar,numbers))
ans1 =list(map(lambda a : a**2,numbers))
print(ans)
print(ans1)


# def squar_1(b):
#     return b**2

# numbers=[1,2,3,4,5,6]
# ans =list(filter(squar_1,numbers))
# print(ans)
