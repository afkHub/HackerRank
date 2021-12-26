# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input().split()
N = s[0]
M = int(N)*3

width = int(M)

for i in range(int(N)):
    if i != round(int(N)//2) and i < round(int(N)//2):
        print (('.|.'*(i*2+1)).center(width,'-'))
    elif i == round(int(N)//2):
        print ("WELCOME".center(width,'-'))
    else:
        print (('.|.'*((int(N)-1-i)*2+1)).center(width,'-'))

