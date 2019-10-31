#text=input("Enter the text to be added to a file")
#fptr=open("abc.txt","w")
#fptr.write(text)
#fptr.close()


'''function which accepts a filename reads its entire content.
It then finds the count of words in the file'''


def wordCount(filename):
    fptr=open(filename,"r")

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

    fptr.close()
    return wordDict
    





filename="abc" #to use another file change this name

filename=filename+".txt"

#function call
wordDict=wordCount(filename)



print("WORD COUNT")

for i in wordDict:
    print(i,' : ',wordDict[i])



