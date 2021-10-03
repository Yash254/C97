string=input("enter a sentance")
charactersCount=0
wordCount=1
for i in string:
    charactersCount=charactersCount+1
    if(i==" "):
        wordCount=wordCount+1
print("number of characters are-",charactersCount)
print("number of words are-",wordCount)        