def fiboRec(n):
	if n==0:
		return 0;
	if n==1 or n==2:
		return 1;
	else:
		return fiboRec(n-1)+fiboRec(n-2)

def fiboNonRec(n):
	x=0
	y=1
	for i in range(n+1):
		print(f"{x}, ",end='')
		nextTerm = x + y
		x = y
		y = nextTerm
	
	
	
if __name__=='__main__':
	n = int(input("Enter the number: "))
	print(f"Fibonacci for {n} is ") 
	for i in range(n+1):	
		print(f"{fiboRec(i)}, ",end='')	
	
	print(f"\n\nNon rec Fibo of {n}: ")
	print(f"{fiboNonRec(n)}")