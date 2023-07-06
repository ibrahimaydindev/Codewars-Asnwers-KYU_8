def triple_trouble(one, two, three):
    maxLen = max([one, two, three])

    oneList = [*one]
    twoList = [*two]
    threeList = [*three]

    wordListEnd = []

    for i in range(len(maxLen)):
        wordList = oneList[i] + twoList[i] + threeList[i]
        wordListEnd.append(wordList)

    word = "".join(wordListEnd)
    return word
