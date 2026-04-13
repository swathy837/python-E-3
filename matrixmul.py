r1=int(input("enter number of rows of first matrix"))
r2=int(input("enter number of rows of second matrix"))
c1=int(input("enter number of columns of first matrix"))
c2=int(input("enter number of columns of second matrix"))
if c1!=r2:
    print("matrix multiplication not possible")
else:
    A=[]
    B=[]
    print("\nfirst matrix")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input()))
            A.append(row)
    print("\nsecond matrix")
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input()))
            B.append(row)
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            sum=0
            for k in range(c1):
                sum+=A[i][k]*B[k][j]
            row.append(sum)
        result.append(row)
    print("\nresultant matrix...")
    for i in result:
        print(i)
