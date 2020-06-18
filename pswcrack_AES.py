
# -*- coding: utf-8 -*-
"""
Author: Haoming Jin
"""
from datetime import datetime
import pyzipper

# Define all the characters to test
low_charlist = [chr(x) for x in range(ord('a'), ord('z') + 1)]
up_charlist = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
numlist = [str(x) for x in range(0,10)]

# Define the minimum and the maximum password length
MIN = 0
MAX = 5

#You can decide what sets of characters you want to test here
charlist = numlist
charlen = len(charlist)

def extractFile(zipFile, password):
    try:
        zipFile.setpassword(bytes(password,'utf8'))
        zipFile.extractall()
        print("password is " + password)
        with open('psw.txt','w') as f:
            f.write(password)
        return True
    except:
        return False

start = datetime.now()
zipFile = pyzipper.AESZipFile("test.zip")
counter = 0
for i in range(charlen ** MIN, charlen ** MAX):
    temp = i
    Pwd = ''
    while temp:
        Pwd = charlist[temp % charlen] + Pwd
        temp = temp // charlen
    guess = extractFile(zipFile, Pwd)
    if guess: break
    if counter % 10000 == 0:
        print(counter, ' finished', Pwd, ' tested')
    counter += 1
print('time spent: ', datetime.now() - start)
zipFile.close()