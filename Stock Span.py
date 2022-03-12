from sys import stdin

def stockSpan(price,n):
    s=[]
    spans=[]
    s.append(0)
    spans.append(1)
    for i in range(1,n):
        if price[i] <= price[s[-1]]:
            spans.append(1)
            s.append(i)
        else:
            while len(s)>0 and price[i] > price[s[-1]]:
                s.pop() 
            if len(s) == 0:
                spans.append(i+1)
            else:
                spans.append(i-s[-1])
            s.append(i)    
                     
    return spans        
    
	#Your code goes here
def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
