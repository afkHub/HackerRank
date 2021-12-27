# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s = list(map(str, input().split()))
s[0] = sorted(s[0])

a = list(permutations(s[0],int(s[1])))

for i in a:
    print("".join(i))

