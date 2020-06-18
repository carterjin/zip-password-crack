# -*- coding: utf-8 -*-
"""
@author: Haoming Jin
"""
# Writes 000000 - 999999 to a password file, 
# if you already have a passowrd file, just skip this part.
f = open('passdict.txt','w')
for id in range(1000000):
    password = str(id).zfill(6)+'\n'
    f.write(password)
f.close()
#%%
import zipfile

def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd = bytes(password,'utf8'))
        print("password is " + password)
        return True
    except:
        return False
    
zipFile = zipfile.ZipFile("test.zip")
PwdLists = open('passdict.txt')
counter = 0
for line in PwdLists.readlines():
    Pwd = line.strip('\n')
    guess = extractFile(zipFile, Pwd)
    if guess: break
    if counter % 1000 == 0:
        print(counter, ' finished', Pwd, ' tested')
    counter += 1
zipFile.close()