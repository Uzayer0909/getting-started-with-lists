def match_words (words):

    count = 0 

    lst = []


    for word in words:
        if len (word) > 2 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)

    print(lst) 
    return count


words = match_words(["abcd", "madam", "dad","is",])

print(words)