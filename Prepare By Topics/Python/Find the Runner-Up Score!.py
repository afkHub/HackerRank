if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    a = list(arr)
    a.sort()
    a.reverse()
    
    
    reverse= []
    for i in range(len(a)+1):
        if i == 0:
            continue 
        else:
            reverse.append(a[-i])
        
    for i in range(len(reverse)+1):
        if a[i] == a[i+1]:
            continue
        else:
            print(a[i+1])
            break
        

