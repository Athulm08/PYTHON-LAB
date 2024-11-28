def add(*args):
"""
This is a program to add variable length integer arguments passed to the function.
args- It is used pass any number of arguments to a function
"""
return sum(args)
print("The Sum of First 10 numbers:", add(1,2,3,4,5,6,7,8,9,10))
print("\nThe Docstring is:")
print(add.__doc__)
