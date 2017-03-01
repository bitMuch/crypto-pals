#!/usr/bin/python     #
# Created by c@caine  #
# On: 20/02/2017      #
# --- Preamble -------+
import base64                                   	# to encode/decode b64
from sys import argv                            	# for command line arg
# --- Definitions --- #
s = argv[1]
# --- Functions --- #

def hex_to_base64(hex_in):                      	# converts hex to a byte array
  b64_out = base64.b64encode(bytearray.fromhex(hex_in))     
                                                	# then the byte array to b64
  return (b64_out)                              	# spits base back

def main ():
  print(hex_to_base64(s))                         # call function, print to screen
# --- Main --- #
if __name__ == "__main__":
  main()
