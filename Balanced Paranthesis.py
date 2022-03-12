from sys import stdin


def isBalanced(expression) :
	#Your code goes here
    s = []
    for char in expression:
        if char  in '({[':
            s.append(char)
        elif char is ')':
            if (not s or s[-1] != '('):
                return False
            s.pop()
        elif char is '}':
            if (not s or s[-1] != '{'):
                return False
            s.pop()
        elif char is ']':
            if (not s or s[-1] != '['):
                return False
            s.pop()
    if (not s):
        return True

#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
