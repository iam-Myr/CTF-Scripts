#!/bin/python3
from pwn import *
#             123456789012345678901234567890
guess ="ifctf{What?_You_want_more_lambdas?__}"
flag = "ifctf{What__You_want_m__e_lambdas?__}"
pos = ["y","a","o","i","e","u","_","Y","A","O","I","E","U","0","1","3","4",] #for 2
answer = [541982718533, 541752425566, 541920185944, 507556842335, 288512657218, 542133179466, 305508892749, 520052997187]

# 0: 6,7,19 (_ Y e) -
# 1: 5, 17, 18, 29, 30 (?,o,r,_,_)
# 2: 3, 4, 15, 16, 28 (a,t,_,m,?)
# 3: 1, 2, 14, 26, 27 (W,h,t,a,s)
# 4: 12, 13, 24, 25 (a,n,b,d)
# 5: 10, 11, 23 - (_,w,m)
# 6: 9, 21, 22 - (e,l,a)
# 7: 8, 20 (o _)

p = process('./lambda.py')
p.recvline()
p.sendline(guess.encode())

#parsing
test = p.recvline().decode('utf-8').strip().split(">")[1]
test = test.replace("[","").replace("]","").replace(" ","").split(",")
test = [int(x) for x in test]

temp = list(guess)

# get intial intro
for i in range(len(pos)):
    for j in range(122, 33,-1):
        for z in range(122,33, -1):
            p.recvline()

            if(test[1] != answer[1]):
                temp[29+5] = chr(j)
                temp[30+5] = chr(z)
                #temp[16+5] = chr(z)

            string = "".join(temp)
            print(string)
            p.sendline(string.encode())

            #parsing
            test = p.recvline().decode('utf-8').strip().split(">")[1]
            test = test.replace("[","").replace("]","").replace(" ","").split(",")
            test = [int(x) for x in test]
p.close()
