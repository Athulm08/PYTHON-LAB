number = int(input("Enter a number to find its factors: "))
divisor = 1
print(f"Factors of {number} are:")
while divisor <= number:
if number % divisor == 0:
print(divisor)
divisor += 1
