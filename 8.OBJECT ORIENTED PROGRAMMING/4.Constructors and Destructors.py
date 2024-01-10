class cont_dest:
    x = 0
    
    def __init__(self,color,type):
        self.color=color
        self.type =type
        print('Constructed')

    def __del__(self):
        print('Destructor')

cd = cont_dest('Black','SUV')
print(cd.color)
print(cd.type)

cd_1 = cont_dest('Red','sedan')
print(cd_1.color)
print(cd_1.type)
