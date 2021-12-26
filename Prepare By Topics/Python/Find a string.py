def count_substring(string, sub_string):

    s = list(string)
    s = ''.join(s)

    a = []
    a.append(s)
    
    counter = 0
    for i in range(len(string)):
            if a[0][i:i+len(sub_string)] == sub_string:
                counter += 1
                
                
    return counter
            
if __name__ == '__main__':
