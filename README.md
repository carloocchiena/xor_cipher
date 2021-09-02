# xor_cipher

The XOR Encryption algorithm is a very effective yet easy to implement method of symmetric encryption. Due to its effectiveness and simplicity, the XOR Encryption is an extremely common component used in more complex encryption algorithms used nowadays.

It operates according to the principles:

A {\displaystyle \oplus }\oplus  0 = A,
A {\displaystyle \oplus }\oplus  A = 0,
A {\displaystyle \oplus }\oplus  B = B {\displaystyle \oplus }\oplus  A,
(A {\displaystyle \oplus }\oplus  B) {\displaystyle \oplus }\oplus  C = A {\displaystyle \oplus }\oplus  (B {\displaystyle \oplus }\oplus  C),
(B {\displaystyle \oplus }\oplus  A) {\displaystyle \oplus }\oplus  A = B {\displaystyle \oplus }\oplus  0 = B,
where {\displaystyle \oplus }\oplus  denotes the exclusive disjunction (XOR) operation.[2] This operation is sometimes called modulus 2 addition (or subtraction, which is identical).[3] With this logic, a string of text can be encrypted by applying the bitwise XOR operator to every character using a given key. To decrypt the output, merely reapplying the XOR function with the key will remove the cipher.

Text Credits:

<a href ="https://en.wikipedia.org/wiki/XOR_cipher">Wikipedia</a>
<a href ="https://www.101computing.net/xor-encryption-algorithm/">101 Computing</a>
