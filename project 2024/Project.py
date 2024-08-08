
'''
class student:
    def __init__(self,naam,marks):
        self.naam=naam
        self.marks= marks
    def get_avg(self):
        sum = 0
        for a in self.marks:
            sum+=a
        sum/=len(self.marks)
        print (f'{self.naam} avg score is {sum}')
    @staticmethod
    def hi_bol():
        print('hi')
        
        
s1 = student('lol',[56,87,90])
s1.get_avg()
''''''
class banku:
    def __init__(self,balance,number):
        self.balance= balance
        
        self.num= number
    def debit(self,amount):
        self.balance+=amount
    def credit (self,amount):
        self.balance-=
        amount
    def amountshow(self):
        print (f'The balance is {self.balance}')
b1=banku(8000,6789461)
b1.debit(897)
b1.amountshow()
'''

'''
class circle:
    import math
    def __init__(self,radi):
        self.radi=radi
    def area(self):
        print(f'The area of circle is {3.14*self.radi**2}')
    def pari(self):
        print(f'the perimeter is {2*3.14*self.radi}')

c1= circle(8)
c1.area()
c1.pari()
''''''
import sys
from cryptography.fernet import Fernet
def write_key():
    k = Fernet.generate_key()
    with open('key.key','wb') as kfile:
        kfile.write(key)
def load_key():
    return open('key.key','rb').read()
def ad():
    acc=input('Enter the account number')
    pas = input('Enter  the password')
    with open('FILE.txt','a') as f:
        f.write(acc+ ' ' + pas)
def vie():
    with open('file.txt','r') as f:
        a = f.readlines()
    for b in a:
        u ,p = b.split()
        print(f'account {u} password {p}')
while True:
    pwd = str(input('enter the password(enter q for exit)'))
    if (pwd=='haha'):
        print('welcome')
        break
    elif (pwd=='q'):
        sys.exit()    
    else:
        print('aap galat hai')
        continue
fun = input('What you what to do(add/view)')
if (fun=='add'):
    ad()
elif (fun=='view'):
    vie()
else:
    print('enter a valid thing')
''''''
#                                                                                    ####Pig game####
import sys
def win():
    sc=0
    if (p1 >=50):
        print('player 1 won')
        sys.exit()
    elif(p2 >=50):
        print('player 2 won')
        sys.exit()   
import random
p1= 0
p2 = 0
sc=0
while True:
    win()
    print('player 1 score ',p1)
    while True:
        print('player 1 turn')
        rol = random.randint(1,6)
        print('the dice rolled to',rol)
        inp = input('do you want play(y/n)')
        if (rol==1):
            sc=0
            rol=0
        sc+=rol
        if (inp=='y'):
            pass
        elif (inp=="n"):
            p1+=sc
            break
    print('player 2 score',p2)
    win()
    while True:
        print('player 2 turn')
        rol = random.randint(1,6)
        print('the dice rolled to',rol)
        inp = input('do you want play(y/n)')
        if (rol==1):
            sc=0
            rol=0
        sc+=rol
        if (inp=='y'):
            pass
        elif (inp=="n"):
            p2+=sc
            break
''''''
import random
import time
op = ['+','-','*']
ans=0
def ranq():
    f = random.randint(3,12)
    l=random.randint(3,12)
    o = random.choice(op)
    epr = str(f) + o + str(l)
    ans = eval(epr)
    print(epr)
    return (ans)
input('press any key to start (press q end)')
st =time.time()
w=0
tot=0
while True:
    ans = ranq()
    a = (input('enter your answer'))
    if (a=="q"):
        break
    elif (int(a)!=ans):
        w+=1
    tot+=1
et=time.time()
print(f'you solved {tot} question,out of which {w} where wroung and completed in {et-st} seconds')
''''''
#                                                                        ####slot machine(prob for future me)####
import random
def dep():
    while True:
        am= input('enter the amount')
        if (am.isdigit()):
            if(am > 0):
                am = int(am)
                break
            else:
                print('amount should be greater then 0')
        else:
            print('Enter a  valid amount')
    return (am)
MAX_LINE=3
def lin():
    while True:
        lin= input('enter the number of lines')
        if (lin.isdigit()):
            lin= int(lin)
            if (1< int(lin) <=MAX_LINE):
                break
            else:
                print(f'no. of line shoulld be greater than 1 and lesss than {MAX_LINE}')
        else:
            print('Enter a  valid amount')
    return (lin)
MAX_BET = 100
MIN_BET=1
def bet():
    while True:
        bet= input('enter the number of bet')
        if (bet.isdigit()):
            bet= int(bet)
            if (MIN_BET< int(bet) <=MAX_BET):
                break
            else:
                print('bet should be greater then 1 and less then 100')
        else:
            print('Enter a  valid bet')
    return (bet)
def inter():
    dep = dep()
    while True:
        lin = lin()
        bet = bet()
        total_bet = bet*lin
        while True:
            if (total_bet>=dep):
                print('Your total amount of bet is greter than your deposit')
                lin = lin()
                bet = bet()
            else:
                break
        i = input(f'you are betting {bet} on {lin} which equal to {total_bet} press c to confirm r to renter')
        if (i=="c"):
            break
rows = 3
cols =3
syms={'h':1,'hm':2,'hmm':4,'hmmm':5}
def get_spin(rows,cols,syms):
    all_sym =[]    
    for sym,sym_c in syms.items():
        for _ in range(sym_c):
            all_sym.append(sym)
    col = []
    exp_lis= all_sym.copy()
    for _ in range(cols) :
        va = random.choice(all_sym)
        col.append([va])
        exp_lis.remove(va)
    return col
def prin(col):
    for row in range(col[0]):
        for i,colum in enumerate(col):
            if i!=(len(col)-1):
                print (colum[row],end="|")
            else:
                print(colum , end="")    
        print()
''''''
#                                                                  ####turtle racing####
from mimetypes import init
import turtle
import random
import time

width , height = 500,500
def khiladi_pucho():
    while True:
        racers= input('Enter the number of racer between 2 - 10')
        if racers.isdigit():
            racers = int(racers)
            if (2<= racers <= 10):
                break
            else:
                print('enter a number between 2-10')
                continue
        else:
            print("enter a valid number")
            continue
    return (racers)
def init_turtle():
    screen =turtle.Screen()
    screen.setup(width,height)
    screen.title('turtle racing')
def create_turtles():
    colours= ['red','green','blue','yellow','orange','black','purple','pink','brown','cyan']
    random.shuffle(colours)
    color = colours[:racers]
    turtles = []
    spac = 0
    for i,colors in enumerate(color):
        khiladi = turtle.Turtle()
        khiladi.color(colors)
        khiladi.shape("turtle")
        khiladi.left(90)
        khiladi.penup()
        khiladi.setpos((spac-200),(-height//2)+50)
        khiladi.pendown()
        turtles.append(khiladi)
        spac+=width/racers
    return (turtles)
def race_them():
    turtles = create_turtles()
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y>= (height//2 -10):
                colors =turtles.index(racer)
    time.sleep(3)
racers = khiladi_pucho()
init_turtle()
race_them()
input()
'''
#                                                                           ###type meter###
'''import curses
from curses import wrapper
def startscreen(stdscr):
    stdscr.clear()
    stdscr.addstr('program')
    stdscr.refresh()
    stdscr.getkey()
def test(stdscr):
    target = "hii tum kon ho"
    inpu = []
    while True:
        stdscr.clear()
        stdscr.addstr(target)
        inp=stdscr.getkey()
        for char in inpu:
            stdscr.addstr(char,curses.color_pair(1))
        stdscr.refresh()
        if ord(inp) == 27:
            break
        if inp in ['KEY_BACKSPACE','\b']:
            if len(inpu) > 0:
                inpu.pop()
        else:
            inpu.append(inp)

def tester(stdscr,target,inpu,wpm=0):
    stdscr.clear()
    stdscr.addstr(target)
    stdscr.refresh()


        
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    startscreen(stdscr)
    test(stdscr)

wrapper(main)
''''''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
lis = []
for a in range(x):
    for b in range(y):
        for c in range(z):
            s=0
            p = [a,b,c]
            print(p)
            for _ in p:
                s+=_
            if (s!=n):
                lis.append(p)
print(lis)
'''

i = input().split()
i=list(map(int,i))
print(i)