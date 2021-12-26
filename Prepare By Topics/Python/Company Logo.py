#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s = sorted(list(s))
    
    dicti = {i:s.count(i) for i in s}

    a = dict(sorted(dicti.items(), reverse= True,key=lambda item: item[1]))
    b= list(a)

    b= b[0:3]
    
    for i in range(len(b)):
        print(b[i], a[str(b[i])])

"""
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s = list(s)
    
    dicti = {i:s.count(i) for i in s}

    a = dict(sorted(dicti.items(), reverse= True,key=lambda item: item[1]))
    
    b= list(a)
    
    x=0
    for times in range(len(b)):
        for i in range(len(b)-1):
            if a[str(b[i])] == a[str(b[i+1])] and (b[i] > b[i+1]):
                x = b[i+1]
                b[i+1] = b[i]
                b[i] = x
        
    
    for i in range(len(b)):
        print(b[i], a[str(b[i])])
"""
