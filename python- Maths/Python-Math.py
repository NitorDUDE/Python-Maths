import os
import time

Black = '\033[30m'
Red = '\033[31m'
Green = '\033[32m'
Yellow = '\033[33m'
Blue = '\033[34m'
Magenta = '\033[35m'
Purple = '\033[36m'
White = '\033[37m'
def cls():
 os.system("cls") if os.name=='nt' else os.system("clear")
def writeway(text,delay):
  for good in text:
    print(good,end='',flush=True)
    time.sleep(delay)
cls()
eye=f'''{Red}
                  ████████████████████████            
              ████████████████████      ██████        
    ██      ████  ████████████    ██      ██████      
      ████████  ██████████████      ██      ██████    
  ██    ████    ████████████████    ██        ████████
    ██████      ██████████████████████        ██████  
██    ████      ██▒▒▒▒██████████▒▒▒▒██        ████    
  ████          ██▒▒▒▒██████████▒▒▒▒██        ██      
                ██▒▒▒▒██████████▒▒▒▒██        ██      
                ██▒▒▒▒▒▒██████▒▒▒▒▒▒██      ██        
                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                
                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██            
              ██████████████████████████              
        {Blue}Greeting from {Purple} team illusion
'''
banner = f'''{Purple}
                __  .__                                            __  .__     
______ ___.__._/  |_|  |__   ____   ____             _____ _____ _/  |_|  |__  
\____ <   |  |\   __\  |  \ /  _ \ /    \   ______  /     \\__  \\   __\  |  \\
|  |_> >___  | |  | |   Y  (  <_> )   |  \ /_____/ |  Y Y  \/ __ \|  | |   Y  \\
|   __// ____| |__| |___|  /\____/|___|  /         |__|_|  (____  /__| |___|  /
|__|   \/                \/            \/                \/     \/          \/ 
             {Red}[developer🗿: {Blue}abhi nitor :){Red}]{White} 
'''
writeway(eye,0.003)
wt = f"{Red}PLEASE WAIT A WHILE!!{White}"

cls()
print(eye)
def loop():
    try:
        time.sleep(0.3)
        cls()
        print(banner)
        print()
        print(f"{Red}---MENU---{White}")
        print(f"{Blue}-1.PERIMETER")
        print("-2.area")
        print("-3.volume")
        print("-4.help")
        print(f"-5.exit{White}")
        print()
        first = int(input(f"{Red}ENTER YOUR CHOICE[1/2/3/4]: {Purple}"))
        if first == 1:
            def periloop():
                try:
                    cls()
                    print(banner)
                    print(wt)
                    time.sleep(0.5)
                    cls()
                    print(banner)
                    print()
                    print(f"{Red}---PERIMETER---")
                    print(f"{Blue}-1.RECTANGLE")
                    print("-2.SQUARE")
                    print("-3.CIRCLE")
                    print(f"-4.TRIANGLE")
                    print(f"-5.GO BACK{White}")
                    print()
                    ch = int(input(f"{Red}ENTER TOUR CHOICE:{Purple}  "))
                    if ch == 1:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        l = int(input(f"{Red}ENTER THE LENGTH: {Purple}"))
                        b = int(input(f"{Red}ENTER THE BREADTH: {Purple}"))
                        print()
                        print(f"{Green}THE PERIMETER OF RECTANGLE IS {Red}{ 2*(l*b)} {White}")
                        time.sleep(15)
                        loop()
                    elif ch == 2:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        l=int(input(f"{Red}ENTER THE LENGTH:{Purple} "))
                        print()
                        print(f"{Green}THE PERIMETER OF SQUARE IS {Red}{4*l}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==3:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        r=int(input("ENTER THE RADIOUS:"))
                        print(f"PERIMETER OF CERCLE IS{2*3.14*r}")
                        time.sleep(15)
                        loop()
                    elif ch==4:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        a=int(input(f"{Red}ENTER THE SIZE OF FIRST SIDE: "))
                        b=int(input("ENTER THE SIZE OF SECOND SIDE: "))
                        c=int(input("ENTER THE SIZE OF THIRD SIDE: "))
                        print(f"{Green}THE AREA OF RECTANGLE IS{Red} {a+b+c}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==5:
                        print(wt)
                        loop()
                    else:
                        print("OPTION NOT AVAILABLE!!")
                        time.sleep(1)
                        periloop()
                except:
                    print(f"{Red}YOU HAVE ENTERED SOMETHING WRONG... ")
                    time.sleep(1)
                    cls()
                    periloop()
            periloop()
        elif first==2:
            def arealoop():
                try:
                    cls()
                    print(banner)
                    print(wt)
                    time.sleep(0.5)
                    cls()
                    print(banner)
                    print()
                    print(f"{Red}---AREA---")
                    print(f"{Blue}-1.RECTANGLE")
                    print("-2.SQUARE")
                    print("-3.CIRCLE")
                    print(f"-4.TRIANGLE")
                    print(f"-5.GO BACK{White}")
                    print()
                    ch = int(input(f"{Red}ENTER TOUR CHOICE:{Purple}  "))
                    if ch == 1:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        l = int(input(f"{Red}ENTER THE LENGTH: {Purple}"))
                        b = int(input(f"{Red}ENTER THE BREADTH: {Purple}"))
                        print()
                        print(f"{Green}THE AREA OF RECTANGLE IS {Red}{l*b} {White}")
                        time.sleep(15)
                        loop()
                    elif ch == 2:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        l=int(input(f"{Red}ENTER THE LENGTH:{Purple} "))
                        print()
                        print(f"{Green}THE AREA OF SQUARE IS {Red}{l*b}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==3:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        r=int(input(f"{Red}ENTER THE RADIOUS:{Purple} "))
                        print(f"{Green}THE AREA OF CIRCLE IS {Red}{3.14*r^2}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==4:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        a=int(input(f"{Red}ENTER THE BASE: "))
                        b=int(input("ENTER THE HIGHT: "))
                        int(print(f"{Green}THE AREA OF TRIANGLE IS{Red} {a*b*0.5}{White}"))
                        time.sleep(15)
                        loop()
                    elif ch==5:
                        print(wt)
                        loop()
                    else:
                        print("OPTION NOT AVAILABLE!!")
                        time.sleep(1)
                        arealoop()
                except:
                    print(f"{Red}YOU HAVE ENTERED SOMETHING WRONG... ")
                    time.sleep(1)
                    cls()
                    arealoop()
            arealoop()
        elif first==3:
            def volloop():
                try:
                    cls()
                    print(banner)
                    print(wt)
                    time.sleep(0.5)
                    cls()
                    print(banner)
                    print()
                    print(f"{Red}---VOLUME---")
                    print(f"{Blue}-1.CUBOID")
                    print("-2.CUBE")
                    print("-3.CYLENDER")
                    print(f"-4.PERAMID")
                    print(f"-5.GO BACK{White}")
                    print()
                    ch = int(input(f"{Red}ENTER TOUR CHOICE:{Purple}  "))
                    if ch == 1:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        l = int(input(f"{Red}ENTER THE LENGTH: {Purple}"))
                        b = int(input(f"{Red}ENTER THE BREADTH: {Purple}"))
                        h = int(input(f"{Red}ENTER THE HIGHT: {Purple}"))
                        print()
                        print(f"{Green}THE VOLUME OF CUBOID IS {Red}{ l*b*h} {White}")
                        time.sleep(15)
                        loop()
                    elif ch == 2:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        l=int(input(f"{Red}ENTER THE LENGTH:{Purple} "))
                        print()
                        print(f"{Green}THE VOLUME OF CUBE IS {Red}{l*l*l}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==3:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        r=int(input(f"{Red}ENTER THE RADIOUS:{Purple} "))
                        r=int(input(f"{Red}ENTER THE HIGHT:{Purple} "))
                        print(f"{Green}THE PERIMETER OF CYLENDER IS {Red}{3.14*r^2*h}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==4:
                        cls()
                        print(banner)
                        print(wt)
                        time.sleep(0.5)
                        cls()
                        print(banner)
                        cls()
                        l=int(input(f"{Red}ENTER THE LENGTH:{Purple}"))
                        w=int(input(f"{Red}ENTER THE WIDTH:{Purple}"))
                        h=int(input(f"{Red}ENTER THE HIGHT:{Purple}"))
                        print(f"{Green}THE VOLUME OF PYRAMID IS {Red}{1/3*l*w*h}{White}")
                        time.sleep(15)
                        loop()
                    elif ch==5:
                        print(wt)
                        loop()
                    else:
                        print("OPTION NOT AVAILABLE!!")
                        time.sleep(1)
                        volloop()
                except:
                    print(f"{Red}YOU HAVE ENTERED SOMETHING WRONG... ")
                    time.sleep(1)
                    cls()
                    volloop()
            volloop()
        elif first==4:
            cls()
            time.sleep(0.3)
            print(banner)
            print(f"{Magenta}-This the verson 1.0 of the program")
            print("-This programm is used to help you with your Maths")
            print("-this is the first version of the prograamm so, dont expect too much")
            print()
            print("-Program devloper: NitorDUDE")
            time.sleep(10)
            loop()
        elif first == 5:
            print(f"Exiting...{White}")
            time.sleep(1)
            pass
        else:
            print(f"{Red}YOUR OPTION IS NOT AVAILABLE!!")
            time.sleep(1)
            loop()
    except:
        print(f"{Red}YOU HAVE ENTERED SOMETHING WRONG...")
        time.sleep(1)
        cls()
        loop()
loop()
