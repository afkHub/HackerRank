# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections

n = int(input())
shoes = map(int, input().split())
shoes = collections.Counter(shoes)

bucket = 0

customers = int(input())
for i in range(customers):
    size, price = map(int, input().split())
    if size in shoes and shoes[size] != 0:
        bucket += price
        shoes[size] -= 1

print(bucket)

