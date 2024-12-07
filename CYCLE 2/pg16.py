n = int(input(" enter the range of 1st dict: "))
d = {}
for i in range(n):
key=input("enter the key: ")
val=int(input("enter the val: "))
d[key]=val
n1 = int(input(" enter the range of 2nd dict :"))
d1 = {}
for i in range(n1):
key1=input("enter the key: ")
val1=int(input("enter the val: "))
d1[key1]=val1
merged_dict=d.copy()
merged_dict.update(d1)
print("merged dictionary:",merged_dict)
