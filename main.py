from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import sys

# Load the key and IV from the file
try:
    with open("./keys/mykey.key", "r") as key_f:
        lines = key_f.readlines()
except:
    print("Une erreur est survenue lors du chargement de la cle")
    sys.exit(1)

key_base64 = lines[0].strip()
init_vector_base64 = lines[1].strip() 
key = b64decode(key_base64)
init_vector = b64decode(init_vector_base64)

# Encrypt function 
def encrypt_f(file_location):
    try:
        with open(file_location, "r") as inp_f:
            content = inp_f.read()
    except:
        print("Une erreur est survenue lors de la lecture du fichier")
        sys.exit(1)
    
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    encrypted_content = cipher.encrypt(pad(content.encode(), AES.block_size))

    # Save the encrypted content to a file
    try:
        with open(file_location + ".enc", "wb") as out_f:
            out_f.write(b64encode(encrypted_content))
    except:
        print("Une erreur est survenue lors de la sauvegarde")
        sys.exit(1)

# Decrypt function
def decrypt_f(file_location):
    try:
        with open(file_location, "r") as inp_f:
            encrypted_content = inp_f.read()
    except:
        print("Une erreur est survenue lors de la lecture du crypte")
        sys.exit(1)

    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    encrypted_content = b64decode(encrypted_content)
    decrypted_content = cipher.decrypt(encrypted_content)

    # Save the decrypted content to a file
    try:
        with open(file_location.replace("enc", "dec"), "w") as out_f:
            out_f.write(unpad(decrypted_content, AES.block_size).decode())
    except:
        print("Une erreur est survenue lors de la sauvegarde du fichier dechiffre")
        sys.exit(1)

if __name__ == "__main__":
    decrypt_f("./files/test.enc")