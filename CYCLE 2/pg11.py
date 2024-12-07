lst=input("enter the list of words:").split()
maxlength=max(len(word)for word in lst)
lword=[word for word in lst if len(word)==maxlength]
print(f"the largestword word:{lword},size:{maxlength}")
