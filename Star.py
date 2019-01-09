import sys
data = input("Enter a number:")
num = int(data)
_num = num+1

for i in range(1,_num):
    for k in range(_num-i,1,-1):
        print(" ",end='')
    for j in range(1,2*i):
        print("*",end='')
    print()
for i in range(_num,1,-1):
    for j in range(i-_num,1,+1):
        print(" ",end='')
    for k in range(1,i*2-4):
        print("*",end='')
    print()

