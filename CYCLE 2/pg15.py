def convert(lst):
res_dict = {}
for i in range(0, len(lst), 2):
res_dict[lst[i]] = lst[i + 1]
return res_dict
userdict = dict()
count = int(input("enter the number of entries in dictionary : "))
for i in range(count):
key = input("enter the key : ")
value = input("enter the value : ")
userdict[key] = value
print("original dictionary : ")
print(userdict)
print("key - ascending order sort")
a = convert((sorted(userdict.items())))
print(a)
print("key - descending order sort")
b = convert(sorted(userdict.items(), reverse = true))
print(b)
print("value - asccending order sort")
c = convert(sorted(userdict.items(), key=lambda item: item[1],))
print(c)
print("value - descending order sort")
d = convert(sorted(userdict.items(), key=lambda item: item[1], reverse=true))
print(d)
