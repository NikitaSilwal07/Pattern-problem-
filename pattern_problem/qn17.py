n=5
for i in range(n):

    for j in range(i,n):
        print(" ", end = ' ')

    for j in range(i):
        print(j+1, end = ' ')   

    for j in range(i+1,0,-1):
        print(j, end = ' ')    
    print(' ')