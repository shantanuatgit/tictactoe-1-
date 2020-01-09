while True:
    first_move=input('If you want to go first press 1\n'
                     'If you ant to go second press 2\n'
                     'Press 3 to EXIT\n')
    if first_move==2:
        from functions import *
        from winfunctions import *
        import random
        a=['1','2','3']
        b=['4','5','6']
        c=['7','8','9']
        checklist=[None]*9
        j=0
        while j<9:
            checklist[j]=0
            j=j+1
        chance=0
        i=0
        while (1):
            if i%2!=0:
                while True:
                        x=input('Enter location of X')
                        if x<=9:
                            checklist[x-1]=checklist[x-1]+1
                            if checklist[x-1]==1:
                                break
                            else:
                                print "Enter valid move"
                        elif x>9:
                            print "Enter valid move"
                if x<=3:
                    a[x-1]='X'
                    chance=chance+1
                elif x<=6:
                    b[x-4]='X'
                    chance=chance+1
                elif x<=9:
                    c[x-7]='X'
                    chance=chance+1
                L=check_row(a,b,c)
                M=check_col(a,b,c)
                N=check_diag(a,b,c)
                if(L==1 or M==1 or N==1):
                    print a,'\n',b,'\n',c,'\n',
                    break
            if i%2==0 or i==0:
                if i==0:
                    while (1):
                        t=random.randint(1,9)
                        if checklist[t-1]<1:
                            y=t
                            break
                elif i==2:
                    while (1):
                        t=random.randint(1,9)
                        if checklist[t-1]<1:
                            y=t
                            break
                else:
                    y1=check_col_win(a,b,c)
                    y2=check_row_win(a,b,c)
                    y3=check_diag_win(a,b,c)
                    if y1>=1:
                        y=y1
                    elif y2>=1:
                        y=y2
                    elif y3>=1:
                        y=y3
                    else:
                        while (1):
                            t=random.randint(1,9)
                            if checklist[t-1]<1:
                                y=t
                                break
                if y<=9:
                    checklist[y-1]=checklist[y-1]+1
                    if checklist[y-1]==1:
                        if y<=3:
                            a[y-1]='Y'
                            chance=chance+1
                        elif y<=6:
                            b[y-4]='Y'
                            chance=chance+1
                        elif y<=9:
                            c[y-7]='Y'
                            chance=chance+1
                        print a,'\n',b,'\n',c,'\n',
                        l=check_row(a,b,c)
                        m=check_col(a,b,c)
                        n=check_diag(a,b,c)
                        if(l==1 or m==1 or n==1):
                            print a,'\n',b,'\n',c,'\n',
                            break
            i=i+1
            if chance==9:
                print "GAME TIED\n"
                break
    if first_move==1:
        from functions import *
        from winfunctions import *
        import random
        a=['1','2','3']
        b=['4','5','6']
        c=['7','8','9']
        checklist=[None]*9
        j=0
        while j<9:
            checklist[j]=0
            j=j+1
        print a,'\n',b,'\n',c,'\n',
        chance=0
        i=0
        while (1):
            if i%2==0 or i==0:
                while True:
                        x=input('Enter location of X')
                        if x<=9:
                            checklist[x-1]=checklist[x-1]+1
                            if checklist[x-1]==1:
                                break
                            else:
                                print "Enter valid move"
                        elif x>9:
                            print "Enter valid move"
                if x<=3:
                    a[x-1]='X'
                    chance=chance+1
                elif x<=6:
                    b[x-4]='X'
                    chance=chance+1
                elif x<=9:
                    c[x-7]='X'
                    chance=chance+1
                L=check_row(a,b,c)
                M=check_col(a,b,c)
                N=check_diag(a,b,c)
                if(L==1 or M==1 or N==1):
                    print a,'\n',b,'\n',c,'\n',
                    break
            if i%2!=0:
                if i==1:
                    if x==5:
                        y=1
                    elif x!=5:
                        y=5
                else:
                    y1=check_col_win(a,b,c)
                    y2=check_row_win(a,b,c)
                    y3=check_diag_win(a,b,c)
                    if y1>=1:
                        y=y1
                    elif y2>=1:
                        y=y2
                    elif y3>=1:
                        y=y3
                    else:
                        while (1):
                            t=random.randint(1,9)
                            if checklist[t-1]<1:
                                y=t
                                break
                if y<=9:
                    checklist[y-1]=checklist[y-1]+1
                    if checklist[y-1]==1:
                        if y<=3:
                            a[y-1]='Y'
                            chance=chance+1
                        elif y<=6:
                            b[y-4]='Y'
                            chance=chance+1
                        elif y<=9:
                            c[y-7]='Y'
                            chance=chance+1
                        print a,'\n',b,'\n',c,'\n',
                        l=check_row(a,b,c)
                        m=check_col(a,b,c)
                        n=check_diag(a,b,c)
                        if(l==1 or m==1 or n==1):
                            print a,'\n',b,'\n',c,'\n',
                            break
            i=i+1
            if chance==9:
                print "GAME TIED\n"
                break
    if first_move==3:
        break

