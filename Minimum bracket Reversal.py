from sys import stdin
def countBracketReversals(str) :
    if len(str)%2!=0:
        return -1
    s=[]
    c=0
    for i in str:
        if i=="{":
            s.append(i)
        elif i=="}":
            if not s:
                s.append(i)
            elif s and s[-1]=="{":
                s.pop()
            elif s and s[-1]!="{":
                s.append(i)
    if s:
    	while s:
            c1=s.pop()
            c2=s.pop()
            if c1==c2:
                c+=1
            else:
                c+=2
    return c

#main
print(countBracketReversals(stdin.readline().strip()))
