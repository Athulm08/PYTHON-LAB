def compare(s1,s2,n):
        return s1[:n]==s2[:n];
s1=input("enter the first  string:")
s2=input("enter the second string:")
n=int(input("enter  how many numbers to compare:"))
if compare(s1,s2,n):
        print(f" the first {n} characters of the both strings are same");
else:
        print(f"the first {n} characters of both strings are different");
