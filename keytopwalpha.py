def make(key):
    import sys
    import codecs
    import hashlib
    final = []
    h = str(hashlib.sha224(bytes(key,'utf-8')).hexdigest())
    print(h)
    split_strings = [h[index: index + 2] for index in range(0, len(h), 2)]
    print(split_strings)
    v = codecs.decode(h,"hex")
    f = sys.stdout.buffer.write(v)
    print(hex(f))
    print(list(int(f)))

make(input('yooo!: '))


