import string
a = list(string.ascii_lowercase) #list of all alphabet letters

def print_rangoli(size):
    # your code goes here
    
    [row,col] = [size*2 -1, (size + size-1) + (size + size-1)-1]
    #print(row)
    #print(col)
    
    lastChar = (len(a) - size) * (-1)
    #print(lastChar)
    width = col
   
    lst=[]
    bucket1 = ""
    

    for i in range(row):
        if i <= round(row//2):
            bucket1 += a[size-1-i]
            lst.append(bucket1)
    
    for i in range(1,len(lst)):
        for j in range(1,len(lst[-i])):
            lst[-i] = lst[-i] + lst[-i-1][-j]
        
            
    
    lst2 = lst[::-1] #reverse
    #add the letters of the previous one at the end of each one in reverse
    for j in range(1,len(lst2)): #
        lst.append(lst2[j])
    #print(lst2)
    #print(lst)
    
    for i in range(len(lst)):
        print (('-'.join(lst[i])).center(width,'-'))


if __name__ == '__main__':
