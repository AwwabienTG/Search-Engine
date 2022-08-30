import string as s

def search_helper(search):

    indexes = []
    i = 0
    words = []
    new_search = ""

    for char in list(search):
        if char in s.ascii_letters or char == " ":
            new_search = new_search + char.lower()

    del char

    for char in list(new_search):   
        i+=1
        if char == " ":
            indexes.append(i-1)
    
    del i
    del char

    try:
        words.append(new_search[0:indexes[0]])
    except:
        words.append(new_search)

    j = 0
    for index in range(len(indexes)-1):
        del index
        words.append(new_search[indexes[j]+1:indexes[j+1]])
        j+=1


    try:
        words.append(new_search[indexes[len(indexes)-1]+1:len(new_search)])
        return words
    except:
        return words
