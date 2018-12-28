# -*- coding: utf-8 -*-

import hashlib

key_sha = '17fc19d5d0ffa46dbe6a1c7c57e969aa6d5760544d96d5f2b0e96a1f66c7ea4b'

chars = 'abcdefghijklmnopqrstuvwxyz'
complete_list = []

for current in xrange(5):
    a = [i for i in chars]
    for y in xrange(current):
        a = [x+i for i in chars for x in a]
    complete_list = complete_list+a

for testkey in complete_list:
    testkey_sha = hashlib.sha256(testkey).hexdigest()
    if(testkey_sha == key_sha):
        print("Password: ", testkey)
        break

