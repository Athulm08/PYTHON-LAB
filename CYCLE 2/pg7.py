lst1=input("enter list1 lements by space seperated :").split()
lst2=input("enter list2 lements by space seperated :").split()
print("output list :")
print(list(set(lst1)-set(lst2)))
