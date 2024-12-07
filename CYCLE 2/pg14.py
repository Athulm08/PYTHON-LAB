intlist = []
intpositive = []
count = int(input("number of integer you need to enter : "))
print("enter ",count, " integer")
for i in range(count):
val = int(input())
intlist.append(val)
if val % 2 != 0:
intpositive.append(val)
word = input("enter a word : ")
print("(a)")
print("positive numbers : ", intpositive)
print("(b)")
for i in intlist:
print("square of ", i , " = ", i * i)
vowels = []
ordvalue = []
for char in word:
ordvalue.append(ord(char))
if char.upper() in 'aeiou':
vowels.append(char)
print("(c)")
print("vowls : ",vowels)
print("(d)")
print("ordinal values : ", ordvalue)
