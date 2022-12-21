import os,stat
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from os import remove

global c
def encrypt(key, filename):
    os.access(filename, os.R_OK)
    chunksize = 64 * 1024
    outputFile = "(encrypted)" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
    remove(filename)

def decrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename[11:]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
    remove(filename)

def autokey(y):
    A = 'K4dH94Djduf79dT7'
    B = 'Kd6gSU95bfut58Fa'
    C = 'MdsUF79dt3HU68ds'
    D = 'VhSdYH689fdseTC7'
    E = 'NsyTIO748fdswR8N'
    F = 'CraSI97gfrVid69V'
    G = 'OdsiBC689dRVsu69'
    H = 'jGIO748fgrVIDoy8'
    I = 'ZgET57fdejI6d7cT'
    J = 'ihfDUF68gkwVki7M'
    K = 'g558rWAWKcMvyp9f'
    L = '13SGhxoUpRC62ZEe'
    M = 'vTIIe212pqD7Z0nd'
    N = 'uN2rHktamwq7r0i9'
    O = 'rorOIRzKajfjrZm8'
    P = 'XetHhA9wnhufmtVB'
    Q = '7uwXaBw3L1luJQbE'
    R = 'I2ldpoJFRq7zif4e'
    S = 'zteq9eh7TKIioSmE'
    T = 'mkoha8g342d0gdg1'
    U = 'rzycltarw8qsaguv'
    V = 'x92kqdbx4ch64fl6'
    W = 'sjvw605xckulipub'
    X = 'z3ohh76urycmrvzp'
    Y = '13bxrqyxhx7ov4h4'
    Z = '8xeYa2okF3O64Kps'
    if y == 'A':
        c = A
    elif y == 'B':
        c = B
    elif y == 'C':
        c = C
    elif y == 'D':
        c = D
    elif y == 'E':
        c = E
    elif y == 'F':
        c = F
    elif y == 'G':
        c = G
    elif y == 'H':
        c = H
    elif y == 'I':
        c = I
    elif y == 'J':
        c = J
    elif y == 'K':
        c = K
    elif y == 'L':
        c = L
    elif y == 'M':
        c = M
    elif y == 'N':
        c = N
    elif y == 'O':
        c = O
    elif y == 'P':
        c = P
    elif y == 'Q':
        c = Q
    elif y == 'R':
        c = R
    elif y == 'S':
        c = S
    elif y == 'T':
        c = T
    elif y == 'U':
        c = U
    elif y == 'V':
        c = V
    elif y == 'W':
        c = W
    elif y == 'X':
        c = X
    elif y == 'Y':
        c = Y
    elif y == 'Z':
        c = Z
    return c
def getKey1(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def getKey2(password ,y):
    a = open("psw.txt")
    k = password
    s = " "
    while (s):
        s = a.readline()
        l = s.split()
        if k in l:
            f = autokey(y)
            hasher = SHA256.new(f.encode('utf-8'))
    return hasher.digest()

def Main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ")
    z=input("do you want a manual(m) or automatic(a) password")
    y=input("enter the alkey")
    if choice == 'E' or choice == 'e':
        filename = input("File to encrypt: ")
        password = input("Password: ")
        if z=='m':
            encrypt(getKey1(password), filename)
            print("Done.")
        elif z=='a':
            encrypt(getKey2(password, y), filename)
            print("Done.")
    elif choice == 'D' or choice == 'd':
        filename = input("File to decrypt: ")
        password = input("Password: ")
        if z == 'm':
            decrypt(getKey1(password), filename)
            print("Done.")
        elif z == 'a':
            decrypt(getKey2(password, y), filename)
            print("Done.")
    else:
        print("No Option selected, closing...")


if __name__ == '__main__':
    Main()
