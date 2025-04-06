def print_sol():
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=" ")
        print()
    print()

def is_safe(row,col):
    for i in range(col):
        if a[row][i]:
            return False
        
    for i in range(row):
        if a[i][col]:
            return False
    
    for i,j in zip(range(row -1,-1,-1),range(col -1,-1,-1)):
        if a[i][j]:
            return False
        
    for i,j in zip(range(row -1,-1,-1),range(col+1,n)):
        if a[i][j]:
            return False
    
    return True

def nqueen(row):
    if row==n:
        print_sol()
    else:
        for i in range(n):
            if is_safe(row,i):
                a[row][i]=1
                nqueen(row+1)
                a[row][i]=0

n=int(input("Enter value of N: "))
a=[[0]*10 for _ in range(10)]
nqueen(0)

               