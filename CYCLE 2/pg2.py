str=input("enter a string")
d="$"
newstr=str[0] + str[1:].replace(str[0],d)
print(newstr)
