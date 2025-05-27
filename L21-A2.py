list_ = ['abc','xyx','1221','kfc']
def match_words(words):
    count = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count += 1
            lst.append(word)
    print('list of words with the same first and last characters are',lst)
    return count
count = match_words(list_)
print('number of words having the same last and first characters is',count)