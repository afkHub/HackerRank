if __name__ == '__main__':
    
    final =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        
        begin = [name, score]
        final.append(begin)
        
    score = []
    
    for i in range(len(final)):
        score.append(final[i][-1])
    
    score.sort()
    
    for i in range(len(score)):
        if score[i] == score[i+1]:
            continue
        else:
            second = score[i+1]
            break
    
    final.sort()
    for i in range(len(final)):
        if final[i][-1] == second: 
            print(final[i][0])
        else:
            continue
             

            
        
        
        

