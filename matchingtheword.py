def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of word with first and last characters are same",lst)
    return ctr
count = match_words(['abc','cfc','xyz','aba','1221'])
print("number of word having first and last characters same",count)