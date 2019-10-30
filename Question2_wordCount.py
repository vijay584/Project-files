#text=input("Enter the text to be added to a file")
#fptr=open("abc.txt","w")
#fptr.write(text)
#fptr.close()






fptr=open("abc.txt","r")

text=fptr.read()
print(text)

textList=text.split()
print(textList)

wordDict={}

for i in textList:
    if i in wordDict:
        wordDict[i]=wordDict[i]+1
    else:
        wordDict[i]=1


print("WORD COUNT")

for i in wordDict:
    print(i,' : ',wordDict[i])


fptr.close()
