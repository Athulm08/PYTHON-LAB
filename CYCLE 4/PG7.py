def factorial(num):
        if num == 0 or num == 1:
                return 1
        else:
                fact = 1
                for i in range(2, num + 1):
                        fact *= i
                return fact
def series(n):
        sum = 0
        for i in range(1, n + 1):
                term = (i ** i) / factorial(i)
                sum += term
        return sum
n = int(input("Enter the number of terms: "))
print(f"The sum of the series up to {n} terms is: {series(n)}")
