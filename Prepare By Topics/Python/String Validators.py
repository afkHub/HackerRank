if __name__ == '__main__':
    s = input()
    s = list(s)
    
    a = 0
    for i in range(len(s)):
        if s[i].isalnum() == True:
            a += 1
    if a == 0:
        print("False")
    else:
        print("True")
        a = 0

    for i in range(len(s)):
        if s[i].isalpha() == True:
            a += 1
    if a == 0:
        print("False")
    else:
        print("True")
        a = 0
        
    for i in range(len(s)):
        if s[i].isdigit() == True:
            a += 1
    if a == 0:
        print("False")
    else:
        print("True")
        a = 0
    
    for i in range(len(s)):
        if s[i].islower() == True:
            a += 1
    if a == 0:
        print("False")
    else:
        print("True")
        a = 0

    for i in range(len(s)):
        if s[i].isupper() == True:
            a += 1
    if a == 0:
        print("False")
    else:
        print("True")
        a = 0
                    
