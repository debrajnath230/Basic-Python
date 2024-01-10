# Types of interitance

# SIngle level
# Multi Level
#Multiple

#Single Level Heritance

class A:
    def state1(self):
        print("State 1 Presnrt")
        
    def state2(self):
        print("state 2 present")
    
    def state3(self):
        print("state 3 present")
        
class B(A):
    
    def state4(self):
        print("State4 Presnt")
    
    def state5(self):
        print("State5 Presnt")    
        
a= A()
a.state1()
a.state2()

b=B()
b.state4()
b.state5()
b.state1()