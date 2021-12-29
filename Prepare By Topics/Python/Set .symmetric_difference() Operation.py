# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = input()
engNo = list(input().split())

fre = set(input())
freNo = list(input().split())

engSet = set()
for i in range(len(engNo)):
    engSet.add(engNo[i])
freSet = set()
for i in range(len(freNo)):
    freSet.add(freNo[i])

result = engSet.symmetric_difference(freSet)
print(len(result))
