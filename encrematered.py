def enc(wordf,key):
    import random
    random.seed()
    prob = list(",<#>/?;:]}{[|+=(")
    x = random.sample(range(len(prob)), len(prob))
    y = random.sample(range(len(wordf)), int(len(wordf) / 2))
    m = list("abcdef1234567890")
    if key == '':

        for i in prob:
            x[prob.index(i)] = prob[x[prob.index(i)]]
    else:
        x = list(key)

    key = dict(zip(m,x))

    word = list(wordf)
    for e in y:
        word[e] = key[word[e]]
    x = ''.join(word) + 'ꜵ' + ''.join(x)

    return x.split("ꜵ")
