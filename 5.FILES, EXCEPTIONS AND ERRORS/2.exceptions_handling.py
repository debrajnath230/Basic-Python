try:
    a=2
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print('Continue with following code')