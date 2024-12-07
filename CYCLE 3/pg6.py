n = int(input("Enter the Range: "))
Prime_numbers = []
for num in range(2, n + 1):
	prime = True
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
		prime = False
		break
	if prime:
		Prime_numbers.append(num)
		print(f"Alternative Prime Numbers till {n} are:")
		for p in range(0, len(Prime_numbers), 2):
print(Prime_numbers[p])
