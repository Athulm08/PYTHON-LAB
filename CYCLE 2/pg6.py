names=input("enter the names").split(„,‟)
a_count=0
for name in names:
a_count+= name.lower().count('a')
print(f"the letter 'a' has occured {a_count} times in the list")
