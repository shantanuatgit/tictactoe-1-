def check_row(a,b,c):
    for i in range (1):
        if a[i]==a[i+1]==a[i+2]:
            print a[i],"WIN"
            return 1
        elif b[i]==b[i+1]==b[i+2]:
            print b[i],"WIN"
            return 1
        elif c[i]==c[i+1]==c[i+2]:
            print c[i],"WIN"
            return 1
def check_col(a,b,c):
    for i in range (1):
        if a[i]==b[i]==c[i]:
            print a[i],"WIN"
            return 1
        elif a[i+1]==b[i+1]==c[i+1]:
            print a[i+1],"WIN"
            return 1
        elif a[i+2]==b[i+2]==c[i+2]:
            print a[i+2],"WIN"
def check_diag(a,b,c):
    for i in range (1):
        if a[i]==b[i+1]==c[i+2]:
            print a[i],"WIN"
            return 1
        elif a[i+2]==b[i+1]==c[i]:
            print c[i],"WIN"
            return 1
