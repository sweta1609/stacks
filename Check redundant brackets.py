from sys import stdin

def checkRedundantBrackets(expression) :
	# Your code goes here
    s = []
    for i in range (len(expression)):
        if (expression[i] in '(+-/*'):
            s.append(expression[i])
        elif (expression[i] == ')'):
           if s.pop() == '(':
              return 1
           s.pop()
    return 0 
            
            
        



#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
