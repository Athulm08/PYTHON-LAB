sentence = input("enter the sentence : ")
words = sentence.split()
occdict = dict()
for i in words:
	if i in occdict:
		occdict[i] = occdict[i] + 1
	else:
		occdict[i] = 1
print(occdict)
