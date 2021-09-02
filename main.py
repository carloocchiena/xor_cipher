#simple function to implement XOR Encryption - works both side, encryption and decryption

def cipher(string):
    """
    Define a XOR Key of your choice (one char lenght); returns the string.
    """
    xor_key = "c" 
      
    for i in range(len(string)):
        string = (string[:i] + chr(ord(string[i]) ^ ord(xor_key)) + string[i + 1:])
        
    return string

if __name__ == "__main__":
    sample_string = "banana"
