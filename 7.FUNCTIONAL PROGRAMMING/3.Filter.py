#filter (functions ,iterable)

def even(a):
    return a % 2 == 0

numbers =[1,2,3,4,5,6,7,7,8,9]

ans =set(filter(even,numbers))
print(ans)

ans1= set(filter(lambda a: a%2==0,numbers))
print(ans1)

ans2= set(filter(lambda a: a%2==0,range(0,20)))
print(ans2)