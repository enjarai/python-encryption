#!/usr/bin/env python3
from Crypto.Cipher import AES
from tkinter import *
import struct
import base64

class encryption():
    def __init__(self):
        self.salt = "mikaisdikmikaisd"

        self.window = Tk()
        self.window.title("enjarai's AES encryption")

        self.github = Label(self.window, text="source code: https://github.com/enjarai/python-encryption")
        self.input1 = Entry(self.window, width=40, justify="center")
        self.input2 = Entry(self.window, width=20, justify="center")
        self.input1.insert(0, "text")
        self.input2.insert(0, "key")
        self.buttondecrypt = Button(self.window, text="decrypt", command=self.decrypt)
        self.buttonencrypt = Button(self.window, text="encrypt", command=self.encrypt)

        self.github.pack()
        self.input1.pack()
        self.input2.pack()
        self.buttondecrypt.pack(side="left")
        self.buttonencrypt.pack(side="right")

        self.window.mainloop()

    def pad16(self, s):
        return s + "#" * ((16 - len(s) % 16) % 16)

    def unpad16(self, s):
        while s.endswith("#"):
            s = s[:-1]
        return s

    def encrypt(self):
        text = self.input1.get()
        key = self.input2.get()
        cipher = AES.new(self.pad16(key), AES.MODE_ECB)
        ciphertext = base64.b64encode(cipher.encrypt(self.pad16(text)))
        self.input1.delete(0, last=10000)
        self.input1.insert(0, ciphertext)

    def decrypt(self):
        text = self.input1.get()
        key = self.input2.get()
        cipher = AES.new(self.pad16(key), AES.MODE_ECB)
        ciphertext = self.unpad16(cipher.decrypt(base64.b64decode(text)).decode("utf-8"))
        self.input1.delete(0, last=10000)
        self.input1.insert(0, ciphertext)

encryption()
