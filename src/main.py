from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import sys
from generate_key import *

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
            print("Le fichier a ete chiffre avec succes")
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
            print("Le fichier a ete dechiffre avec succes")
    except:
        print("Une erreur est survenue lors de la sauvegarde du fichier dechiffre")
        sys.exit(1)

if __name__ == "__main__":
    while True:
        print("\nMenu Principal")
        print("1. Générer une paire de clé/IV")
        print("2. Chiffrer un fichier")
        print("3. Déchiffrer un fichier")
        print("4. Quitter")
        choice = input("Choisissez une option (1-4) : ")
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Choisissez une option valide (1-4) : ")
        
        if choice == "1":
            key_size = int(input("Taille de la cle (128, 192, 256) : "))
            generate_key(key_size)

        elif choice == "2":
            key_location = input("Chemin de la cle : ")

            # Load the key and IV from the file
            try:
                with open(key_location, "r") as key_f:
                    lines = key_f.readlines()
            except:
                print("Une erreur est survenue lors du chargement de la cle")
                sys.exit(1)

            key_base64 = lines[0].strip()
            init_vector_base64 = lines[1].strip() 
            key = b64decode(key_base64)
            init_vector = b64decode(init_vector_base64)
            file_location = input("Chemin du fichier a chiffrer : ")

            encrypt_f(file_location)

        elif choice == "3":
            key_location = input("Chemin de la cle : ")

            # Load the key and IV from the file
            try:
                with open(key_location, "r") as key_f:
                    lines = key_f.readlines()
            except:
                print("Une erreur est survenue lors du chargement de la cle")
                sys.exit(1)

            key_base64 = lines[0].strip()
            init_vector_base64 = lines[1].strip() 
            key = b64decode(key_base64)
            init_vector = b64decode(init_vector_base64)

            file_location = input("Chemin du fichier a dechiffrer : ")
            decrypt_f(file_location)

        else:
            sys.exit(0)