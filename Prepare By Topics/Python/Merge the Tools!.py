def merge_the_tools(string, k):
    # your code goes here
    s = string
    lst = []
    for i in range(len(s)):
        if i*k <= len(s)-1:
            lst.append(s[i*k:(i+1)*k])

    final=[]
    for j in lst:
        for l in j:
            if l not in final:
                final.append(l)
        print("".join(final))
        final=[]

if __name__ == '__main__':
