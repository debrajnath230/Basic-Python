#lterator

# list =[1,2,3,4,5]
# print(list[2])

# iteration = iter(list)
# print(iteration.__next__())
# print(iteration.__next__())
# print(next(iteration))

#Generator
# def generator():

#     yield 1
#     yield 2
#     yield 2
    
# values =generator()
# print(values.__next__())
# print(values.__next__())

# for i in values:
#     print(i)

# print square from 1 to 5

def squares():
    n=1
    while n <=20:
        squares = n**2
        yield squares
        n=n+1

values = squares()
for i in values:
    print(i)
    