n=int(input("Enter a number to print its Multiplication Table:"))
print("Multiplication Table of ",n,":")
for i in range(1,11):
	print(f"{i}*{n} = {n*i}")
