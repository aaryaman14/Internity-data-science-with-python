# Problem statement 1

import random
def solve(a,b,n):
    c=0
    while(c<3):
        
        print('Try- %d'%(c+1))
        #print(c)
        t=int(input('enter your guess- '))
        if t==n:
            print('Yeah! You identified the number')
            break
        elif t>n:
            print('Please try again! The number you guessed is too high')
        else:
            print('Please try again! The number you guessed is too small')
        
        c=c+1
        
    if c==3:
        print('Oops! All your chances are finished. Better luck next time!')

def main():
    x=int(input('enter start point- '))
    y=int(input('enter end point- '))
    print('You have only 3 chances')
    num=random.randint(x,y)
    solve(x,y,num)

main()