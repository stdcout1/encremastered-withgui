def enc(password, c="LOL"):
    password = str(password)
    password = list(password[2:-1])
    #stolen from my old code
    #changed the key to unicode
    import random
    random.seed()
    #password is decrypted text
    def checkempy():
        for i in y:
            if i == "":
                return True
        return False

    def intcheck():
        for i in y:
            for e in prob:
                if i == e:
                    return True
                else:
                    continue
        return False
    def where(thing):
        for i in y:
            if i == thing:
                return y.index(i)
    def exists(operand):
        for i in y:
            if i == operand:
                return True
        return False

    random.seed()
    y = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    q = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    counter = 0
    prob = list("ἀἐἁἂἑἒἓἃἣἢἡἠἰἱἲἳἴὀὁὂὃὄὅὐὑὒЖ")
    #print (prob)
    #the encrypt list gen
    while checkempy():
        pos = random.randint(0, 26)
        if y[pos] == "":
            for i in prob:
                if not exists(i):
                    y[pos] = i
                    q[pos] = i
        #print(y)
    #import key
    if "ὃ" in c:
        q = c
        y = c

    #print (y)
    #aplhabet LOL
    x = list("abcdefghijklmnopqrstuvwxyz ")
    #replace all numbs with letters
    while intcheck():
         for i in y:
             y[y.index(i)] = x[y.index(i)]
         #print ("yp")

    #print (y)
    e = "".join(q)
    #makesurepw is viable

    def works():
        forb = list("")#every things works!
        for i in password:
            for e in forb:
                if i == e:
                    return False
        return True
    #password switcher


    for i in password:
        #print (password)
        if y.count(i) == 0:
            continue
        else:
            password[password.index(i)] = int(y.index(i))
        #print (y)

    #print (password)
    #password to symbol
    for i in password:
        if isinstance(i, int):
            password[password.index(i)] = str(q[int(i)])
        else:
            continue

    #print(password)

    #combiner
    pasd = "".join(password)
    return pasd + "ꜵ" + e


