def sum_row(a):
    values = []
    rows=len(a)
    cols=len(a[0])
    for i in range(0,rows):
        row_sum= 0
        for j in range(0,cols):  
            row_sum = row_sum+a[i][j]
        values.append(row_sum)
    return values 


def sum_column(a):
    values = []
    rows=len(a[0])
    cols=len(a)
    for i in range(rows):  
        col_sum = 0  
        for j in range(cols):  
            col_sum = col_sum+ a[j][i]
        values.append(col_sum)
    return values 


def non_zero(a):
    a=[0,0,0,0,0,0,1,2,3,4,0,2,4,6,8]
    result=[]
    sum=0
    for num in a:
        if num == 0:
            result.append(sum)
        else:
            sum=sum+num
    return sum


def sum_even(a):
    a=[0,0,0,0,0,0,1,2,3,4,0,2,4,6,8]
    sum=0
    for i in a:
        if i%2==0:
            sum=sum+i
    return sum


def sum_odd(a):
    a=[0,0,0,0,0,0,1,2,3,4,0,2,4,6,8]
    sum=0
    for i in a:
        if i%2!=0:
            sum=sum+i
    return sum


def total_prime(a):
    a=[0,0,0,0,0,0,1,2,3,4,0,2,4,6,8]
    x=[]
    for num in a:
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            x.append(num)
    return len(x)


def diagonal_elements(a):
    values=[]
    n=3
    for i in range(n):
        for j in range(n):
            if i==j:
                values.append(a[i][j])
            else:
                return None
    return values


def sum_diagonals(a):
    sum=0
    n=3
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                sum=sum+a[i][j]
            else:
                return None
    return sum
           

def lower(a):
    row=3
    col=5
    for i in range(0, row):
        for j in range(0, col):
            if (i < j):
                print("0", end = " ")
            else:
                print(a[i][j],end = " " )
        print(" ")


def upper(a):
    row=3
    col=5
    for i in range(0,row):
        for j in range(0,col):
            if (i > j):
                print("0",end=" ")
            else:
                print(a[i][j],end= " ")
        print(" ")


if __name__ == "__main__":
    a = [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]

    ##row sum 
    rs = sum_row(a)
    print(f"row sum: {rs}")

    ## column sum 
    cs = sum_column(a)
    print(f"column sum: {cs}")

    ## non-zero sum
    nz = non_zero(a)
    print(f"non_zero: {nz}")

    ## sum-even 
    se = sum_even(a)
    print(f"sum_even: {se}")

    ## sum-odd
    so = sum_odd(a)
    print(f"sum_odd: {so}")
 
    ## prime number
    pn= total_prime(a)
    print(f"prime number: {pn}")

    ## diagonal elements
    de = diagonal_elements(a)
    print(f"diagonal elements: {de}")

    ## sum diagonal
    sd = sum_diagonals(a)
    print(f"sum diagonal: {sd}")

    ## lower matrixc
    print("lower")
    lm = lower(a)
    
    ## upper matrix
    print("upper")
    um = upper(a)