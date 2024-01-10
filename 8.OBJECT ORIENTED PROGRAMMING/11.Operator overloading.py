# a=1
# b=2
# print(a+b)

# print(int.__add__(a,b))

class vegetables:
    
    def __init__(self , carrot , beans):
        self.carrot=carrot
        self.beans=beans

    def __add__(self,others):
        carrot=self.carrot+ others.carrot
        beans = self.beans + others.beans
        return vegetables(carrot,beans)

v1=vegetables(5,4)
v2=vegetables(7,19)
v3=v1+v2
print(v3.carrot) 
print(v2.beans)  
