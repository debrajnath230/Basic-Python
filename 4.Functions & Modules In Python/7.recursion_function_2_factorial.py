#factorial using recursion
# 0! =1
# 1! =1*0!=1*1=1
# 2! = 1*1*0!=1*1*2=2

def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
result = factorial(40)
print(result)
