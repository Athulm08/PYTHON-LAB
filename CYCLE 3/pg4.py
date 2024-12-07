import math
start = int(input("Enter the start of the range:"))
end = int(input("Enter the end of the range:"))
result = []
for i in range(math.isqrt(start), math.isqrt(end) + 1):
	square = i * i
	if 1000 <= square <= 9999:
		Even = True
		for digit in str(square):
			if int(digit) % 2 != 0:
				Even = False
				break
if Even:
	result.append(square)
	print("Four-digit perfect squares with all even digits:", result)
