def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def encrypt(plaintext, a, b):
    result = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            else:
                result += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(ciphertext, a, b):
    a_inv = modinv(a, 26)
    result = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                result += chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            else:
                result += chr((a_inv * (ord(char) - ord('a') - b)) % 26 + ord('a'))
        else:
            result += char
    return result

def main():
    # Example usage:
    plaintext = "Hello, World!"
    a = 9
    b = 1

    
    encrypted_text = "ivdvwboq"
    
    # Encryption
    #encrypted_text = encrypt(plaintext, a, b)
    #print("Encrypted: ", encrypted_text)

    # Decryption
    decrypted_text = decrypt(encrypted_text, a, b)
    print("Decrypted: ", decrypted_text)

if __name__ == "__main__":
    main()
