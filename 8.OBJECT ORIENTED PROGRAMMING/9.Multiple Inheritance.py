# Multiple Inheritance
class A:
    def state1(self):
        print("State 1 Presnrt")
        
    def state2(self):
        print("state 2 present")
    
    def state3(self):
        print("state 3 present")
        
class B:
    
    def state4(self):
        print("State4 Presnt")
    
    def state5(self):
        print("State5 Presnt")    
        
class C(A,B):
    def state6(self):
        print("State6 Presnt")
    
    def state7(self):
        print("State7 Presnt") 

a=A()
a.state2()

b=B()
b.state5()

c=C()
c.state1()
c.state4()