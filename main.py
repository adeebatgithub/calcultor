
from func import *

class engine:
    
    def __init__(self,inp):
        self.inp = inp
    

    def evl(self):
        
        if self.inp in ['x','done','d']:
            quit()
        
        try:
            self.ans = eval(self.inp)
        except:
            self.ans = False
        
        return self.ans
        
        
        