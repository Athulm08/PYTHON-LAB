lst=[int(num)for num in input("enter a list of numbers(sepaterd by space:").split()]
odd_list=[odd for odd in lst if odd%2!=0]
print(odd_list)
