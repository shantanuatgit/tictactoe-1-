def check_row_win(a,b,c):
    if a[0]=='X' and a[1]=='X' and a[2]!='X' and a[2]!='Y':
        return 3
    elif a[0]=='X' and a[1]!='X' and a[1]!='Y' and a[2]=='X':
        return 2
    elif a[0]!='X' and a[0]!='Y' and a[1]=='X' and a[2]=='X':
        return 1
    elif b[0]=='X' and b[1]=='X' and b[2]!='X' and b[2]!='Y':
        return 6
    elif b[0]=='X' and b[1]!='X' and b[1]!='Y' and b[2]=='X':
        return 5
    elif b[0]!='X' and b[0]!='Y' and b[1]=='X' and b[2]=='X':
        return 4
    elif c[0]=='X' and c[1]=='X' and c[2]!='X' and c[2]!='Y':
        return 9
    elif c[0]=='X' and c[1]!='X' and c[1]!='Y' and c[2]=='X':
        return 8
    elif c[0]!='X' and c[0]!='Y' and c[1]=='X' and c[2]=='X':
        return 7
def check_col_win(a,b,c):
    if a[0]=='X' and b[0]=='X' and c[0]!='X' and c[0]!='Y':
        return 7
    elif a[0]=='X' and b[0]!='X' and b[0]!='Y' and c[0]=='X':
        return 4
    elif a[0]!='X' and a[0]!='Y' and b[0]=='X' and c[0]=='X':
        return 1
    elif a[1]=='X' and b[1]=='X' and c[1]!='X' and c[1]!='Y':
        return 8
    elif a[1]=='X' and b[1]!='X' and b[1]!='Y' and c[1]=='X':
        return 5
    elif a[1]!='X' and a[1]!='Y' and b[1]=='X' and c[1]=='X':
        return 2
    elif a[2]=='X' and b[2]=='X' and c[2]!='X' and c[2]!='Y':
        return 9
    elif a[2]=='X' and b[2]!='X' and b[2]!='Y' and c[2]=='X':
        return 6
    elif a[2]!='X' and a[2]!='Y' and b[2]=='X' and c[2]=='X':
        return 3
def check_diag_win(a,b,c):
    if a[0]=='X' and b[1]=='X' and c[2]!='X' and c[2]!='Y':
        return 9
    elif a[0]=='X' and b[1]!='X' and b[1]!='Y' and c[2]=='X':
        return 5
    elif a[0]!='X' and a[0]!='Y' and b[1]=='X' and c[2]=='X':
        return 1
    elif a[2]=='X' and b[1]=='X' and c[0]!='X' and c[0]!='Y':
        return 7
    elif a[2]=='X' and b[1]!='X' and b[1]!='Y' and c[0]=='X':
        return 5
    elif a[2]!='X' and a[2]!='Y' and b[1]=='X' and c[0]=='X':
        return 3

    
    
