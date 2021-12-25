import textwrap

def wrap(string, max_width):
   
    a = (len(string)/max_width)
    b = round(a)
    if a > b:
        b = b+1
    elif a <= b:
        b = b
    
    char = ""
    for i in range(b):
        if string[i*max_width:(i+1)*max_width] != None:
            char += string[i*max_width:(i+1)*max_width] + "\n"
        else:
            break
    
    return char

if __name__ == '__main__':
