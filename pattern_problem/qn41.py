n = 5  
for i in range(n):
    for j in range(i, -1, -1):  
        print(chr(65 + j), end='')
    print() 

for i in range(n - 2, -1, -1):
    for j in range(i, -1, -1):  
        print(chr(65 + j), end='')
    print() 
