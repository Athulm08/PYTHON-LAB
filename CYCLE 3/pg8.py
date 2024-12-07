limit1 = int(input("Enter the starting range (limit1): "))
limit2 = int(input("Enter the ending range (limit2): "))
for num in range(limit1, limit2 + 1):
	digit_sum = 0
	for digit in str(num):
		digit_sum += int(digit)
		if digit_sum > 1:
			prime = True
			for i in range(2, int(math.sqrt(digit_sum)) + 1):
				if digit_sum % i == 0:
					prime = False
break
if prime:
print(f"Sum of digits of {num} is {digit_sum}, which is a prime.")
