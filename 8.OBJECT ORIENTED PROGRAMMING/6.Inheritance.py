class name:
    x=0
    name =""
    
    def __init__(self,z):
        self.name=z
        print('hi',z)
    
class football_fans(name):
    points = 0
    
    def pts(self):
        print(self.name,'Scores')
        
n=name('Raj')
f =football_fans('Jim')
f.pts()
        