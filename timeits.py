import timeit





def dec(string):
    import numpy as n
    key = list(string.split('ꜵ')[1])
    word = list(string.split('ꜵ')[0])
    m = list("abcdef1234567890")
    chip = dict(zip(key, m))

    for i in word:
        if i in ",<#>/?;:]}{[|+=(":
            word[word.index(i)] = chip[i]
    return ''.join(word)

def dec1(string):
    import numpy as n
    key = list(string.split('ꜵ')[1])
    word = n.array(list(string.split('ꜵ')[0]))
    m = list("abcdef1234567890")
    chip = dict(zip(key, m))
    count = 0
    xd = n.in1d(word, n.array(list(chip.keys())))
    xd2 =n.where(xd == True)
    for x in xd:
        if x:
            word[xd2[0][count]] = chip[word[xd2[0][count]]]
            count += 1
    return ''.join(word)


with open('Low-Resolution-Image-fin.nasir', encoding='utf-8') as f:
    content = f.read().split('.')
    print('0', timeit.timeit(lambda: dec1(content[0]), number=1))
    print('1', timeit.timeit(lambda: dec(content[0]), number=1))