from decremastred import dec
import binascii
from tkinter import *
from tkinter import filedialog
import os
root = Tk()

def dia():
    xd = filedialog.askopenfilenames(initialdir = '/enc', title = 'select your file to encrypt',filetypes = (('text','*.txt'),('all files','*.*')) )

    for i in xd:
        nam = os.path.splitext(i)[0]
        with open('Khimani (HLM) -fin.m4a', encoding='utf-8') as f:
            content = f.read().split('.')
            gg = dec(content[0])
        extension = content[1]
        fp = open("{nam}donzo.{exe}".format(exe = extension, nam = nam), "wb+")
        fp.write(binascii.unhexlify(gg))
        print(extension)
        fp.close()
        print(i)
btn = Button(root, text = 'click to dec', command=dia)
btn.pack()



root.mainloop()

