#!/usr/bin/python3
# Created by c@caine
# On: 12/02/2017
# --- Preamble --- #
import base64 
# --- Definitions --- #
h1 = "1c0111001f010100061a024b53535009181c" 
h2 = "686974207468652062756c6c277320657965" 
b1 = bin(int(h1, 16))[2:]
b2 = bin(int(h2, 16))[2:]
# --- Functions --- #
def xor(x, y):
  
  return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))
#  --- Main --- #
r = xor(b1,b2)

print(str(hex(int(r, base=2)))[2:])

