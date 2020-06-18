# zip-password-crack
A set of Python programs to crack password locked zip file.

### pswcrack.py:
1. Writes number 1-999999 to a file. (If you already have a password file then skip this part)
2. Test out every password in this file.

### pswcrack_custom_list.py:
1. Creates a list of custom combination of upper case, lower case and numbers as possible characters.
2. check every combination of these possible characters with a specified max and min length.
3. Writes the result in a txt file.
speed:16s/100k psw

### pswcrack_AES.py:
Mostly the same as pswcrack_custom_list, but this time it cracks AES encoding.
1. Creates a list of custom combination of upper case, lower case and numbers as possible characters.
2. check every combination of these possible characters with a specified max and min length.
3. Writes the result in a txt file.
speed: 178s/100k psw

Note: I have also tried using concurrent.futures, threading and multiprocessing, but in the end, they either perform worse or just marginally better. So I decided not to include them here.

Also, these programs are only good for shorter passwords or if you already know the passwords are just numbers or just lower case letter. If you include all possible characters, and longer passwords, the calculation time soon becomes unpractical.

I would like to point out that even this very simple program runs faster than the few free or free trial software I am able to find online.
