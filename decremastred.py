def dec(string,key):
    import numpy as n
    word = n.array(list(string))
    m = list("abcdef1234567890")
    chip = dict(zip(list(key),m))
    count = 0
    xd = n.in1d(word, n.array(list(chip.keys())))
    xd2 = n.where(xd == True)

    for x in xd:
        if x:
            word[xd2[0][count]] = chip[word[xd2[0][count]]]
            count += 1

    return ''.join(word)


