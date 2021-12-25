if __name__ == '__main__':
    n = int(input())
    
    a = []
    for i in range(n):
       a.append(i+1)
       
    print(*a, sep = "")

