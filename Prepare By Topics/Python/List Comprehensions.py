if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    final = []
    
    for i in range(x+1):
        for j in range (y+1):
            for k in range (z+1):
                if i+j+k != n:
                    ele = [i,j,k]
                    final.append(ele)
                else:
                    continue
    print(final)

