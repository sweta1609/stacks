from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


def reverseStack(inputStack, extraStack) :
	#Your code goes here
    if (len(inputStack) <= 1):
        return

    while (len(inputStack) != 1):
        #we will pop (len -1)element from s1 and append to s2
        values= inputStack.pop()
        extraStack.append(values)

    lastelement = inputStack.pop()

    while (len( extraStack) != 0): #we will do till s2 stack does not become empty
        values =  extraStack.pop()
        inputStack.append(values) #here we are poping (len -1 )ele from s2 and appending to s2

    reverseStack(inputStack ,  extraStack) #recusrion call
    inputStack.append(lastelement)








'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
