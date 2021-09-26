from encrematered import enc
import os
import binascii
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from decremastred import dec


root = Tk()

'''
change log:
-Remastered enc and dec modules. Now is more optimized and faster.
-changed enc:
    -every other digit (randomly)
-changed dec:
    -uses my best attempt at numpy XD
-fixed set key system
    -I guess i broke it when working with discord?
-file is now ready for inital distribution.



'''

key = StringVar()
Label(root, text = 'Enter Key Below').grid(row = 0, column = 0,padx = 6, pady = 6)
box = Entry(root, textvariable = key)
box.grid(row = 1, column = 0, padx = 6, pady = 6)



def dia():
    xd = filedialog.askopenfilenames(initialdir = '/enc', title = 'select your file to encrypt',filetypes = (('all','*.*'),('all files','*.*')) )

    for i in xd:

        with open(i, 'rb') as f:
            content = f.read()

        sheeh = binascii.hexlify(content)
        savefile = enc(str(sheeh)[2:-1],key.get())
        with open(i, 'w',encoding='utf-8') as f:
            f.write(savefile[0])
            key.set(savefile[1])
        print('E:', i)


def decc():
    if key.get() == '':
        messagebox.showerror('Error', 'No Key Detected')
        return
    xd = filedialog.askopenfilenames(initialdir = '/enc', title = 'select your file to encrypt',filetypes = (('version3','*.*'),('all files','*.*')) )

    for i in xd:
        nam = os.path.splitext(i)[0]
        try:
            with open(i, encoding='utf-8') as f:
                content = f.read()
                gg = dec(content, key.get())
        except:
            messagebox.showerror('Error', 'Invalid file')
            return

        fp = open(i, "wb+")
        fp.write(binascii.unhexlify(gg))
        fp.close()
        print('D:', i)


def info():
    messagebox.showinfo(title = 'Help', message= "Click on encrypt to encrypt a file. If no key is in the text box,"
                                                 " a key will be generated. To decrypt, place key in the box and click"
                                                 " the button. (You can use multiple files at one time)")


btn = Button(root, text = 'Decrypt', command=decc)
btn.grid(row = 0, column = 1, padx = 6, pady = 6)
btn = Button(root, text = 'Encrypt', command=dia)
btn.grid(row = 1, column = 1, padx = 6, pady = 6)
Button(root,text = 'how to use', command = info).grid(row = 2, column = 0, padx = 6, pady = 6, columnspan = 2)



root.mainloop()







