# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations, combinations_with_replacement
s = list(map(str, input().split()))
s[0] = sorted(s[0])

c = list(combinations_with_replacement(s[0],int(s[1])))

for i in c:
    print("".join(i))
