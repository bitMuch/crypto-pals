# /* crypto-pals */
**The Matasano crypto challenges**

As found over at http://cryptopals.com.

(**ch1**): Convert hex to base64
- The string:
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```

- Should produce:
```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```

--

(**ch2**): Fixed XOR
-   If your function works properly, then when you feed it the string: 
```
1c0111001f010100061a024b53535009181c
```
        
- ... after hex decoding, and when XOR'd against:
```
686974207468652062756c6c277320657965
```

- Should produce:
```
686974207468652062756c6c277320657965
```

--



