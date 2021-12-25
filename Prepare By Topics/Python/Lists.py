if __name__ == '__main__':
    N = int(input())
    
    commands = []
    list1 = []

    for i in range(N):
        commands.append(input().split())

        if commands[i][0] == "insert":
            list1.insert(int(commands[i][1]),int(commands[i][2]))
                
        elif commands[i][0] == "print":
            print(list1)
        
        elif commands[i][0] == "remove":
            list1.remove(int(commands[i][1]))    
            
        elif commands[i][0] == "append":
            list1.append(int(commands[i][1]))    
            
        elif commands[i][0] == "sort":
            list1.sort()
            
        elif commands[i][0] == "pop":
            list1.pop()    
            
        elif commands[i][0] == "reverse":
            list1.reverse() 
        