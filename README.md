# xor_cipher

The XOR Encryption algorithm is a very effective yet easy to implement method of symmetric encryption. Due to its effectiveness and simplicity, the XOR Encryption is an extremely common component used in more complex encryption algorithms used nowadays.

It operates according to the principles:

A = A, A A = 0, A B = B A, (A B) C = A (B C), (B A) A = B = B, where
denotes the exclusive disjunction (XOR) operation.
This operation is sometimes called modulus 2 addition (or subtraction, which is
identical).
With this logic, a string of text can be encrypted by
applying the bitwise XOR operator to every character using a given key.
To decrypt the output, merely reapplying the XOR function with the key
will remove the cipher.

Text Credits:

<a href ="https://en.wikipedia.org/wiki/XOR_cipher">Wikipedia</a><br>
<a href ="https://www.101computing.net/xor-encryption-algorithm/">101 Computing</a>


###Usage:

word = cipher("banana")
print (word)


cipher(word)
'banana'
