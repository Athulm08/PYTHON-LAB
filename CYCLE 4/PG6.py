number=list(map(int,input ( "enter the numbers:").split(",")));
multiples=list(filter(lambda x:x%3==0,number));
print(f" the multiples of 3 from the list:{multiples}");
