class simple:
    def __init__(self):
        self.value1=1
        self.value2=2
        
    def __A1__(self):
        print("Abs")
        
    def __B1__(self):
        print("Debraj")
        
s=simple()
print(s.value1)
s.__A1__()
print(s.__A1__())

print(dir(s))
