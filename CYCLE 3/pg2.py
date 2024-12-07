n=int(input("Enter the number to find its fibonacci series:"))
a,b = 0,1
fibonacci=[]
if(n<0):
	print("Enter the number greater than 0")
else:
	for i in range(n):
	fibonacci.append(a)
	a,b = b,a+b
print(f"Fibonacci Series of {n}:{fibonacci}")
