import sys, os, pyaes, binascii

f = open('sensitive-input.txt', 'rb')
f1 = open('encrypted-sensitive-input.txt', 'wb')

#Encrypt input data
key = "Scontain-Germany"
aes = pyaes.AESModeOfOperationCTR(key)
for mess in f.read().split('\n'):
    e_mess = aes.encrypt(mess)
    l = list(ord(c) for c in e_mess);
    e_mess = b''.join(chr(b) for b in l)
    hexlified = binascii.hexlify(e_mess)
    f1.write(hexlified)
    f1.write('\n')

f1.close()
