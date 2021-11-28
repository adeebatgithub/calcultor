from main import engine
from func import error
        
def main():
    
    inp = input('>> ')
    cal = engine(inp)
    ans = cal.evl()
    if ans != False:
        print(f'>> {ans}')
    else:
        error()
        
    
    
while 1:
    main()
    