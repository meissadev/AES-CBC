from Crypto.Random import get_random_bytes
from base64 import b64encode
import sys

def generate_key(key_size):
    if key_size != 128 and key_size != 192 and key_size != 256:
        print("La taille de la cle doit etre 128, 192 ou 256 bits")
        sys.exit(1)

    key = get_random_bytes(int(key_size / 8)) # 128 bit key
    init_vector = get_random_bytes(16) # 128 bit IV

    key_base64 = b64encode(key).decode()
    init_vector_base64 = b64encode(init_vector).decode()

    key_name = input("Nom de la cle: ")

    if key_name.endswith(".key"):
        key_location = "./../keys/" + key_name
    else:
        key_location = "./../keys/" + key_name + ".key"

    try:
        with open(key_location, "x") as key_f:
            key_f.write(key_base64 + "\n" + init_vector_base64)
            print("La cle a ete generee avec succes")

    except FileExistsError:
        print("Cette cle existe deja !")
        sys.exit(1)
