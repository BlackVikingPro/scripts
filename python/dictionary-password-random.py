#!/usr/bin/python
import itertools

res = itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJCKLMNOPQRSTUVWXYZ0123456789", repeat=int(16))
output = open('dictionary-password.txt', 'w+')

for i in res:
    output.write(''.join(i)+"\n")

output.close()