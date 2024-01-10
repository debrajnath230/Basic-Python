#Single Multi Heritance

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
        
class C(B):
    def state6(self):
        print("State4 Presnt")
    
    def state7(self):
        print("State5 Presnt") 

c=C()
c.state6()
c.state7()
c.state1()
c.state5()
