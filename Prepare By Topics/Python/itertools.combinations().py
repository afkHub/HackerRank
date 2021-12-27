# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
s = list(map(str, input().split()))
s[0] = sorted(s[0])

a = []
for i in range(1,1+int(s[1])):
    a.append(list(combinations(s[0],int(s[1])-(int(s[1])-i))))

for j in range(len(a)):
    for i in a[j]:
        print("".join(i))

