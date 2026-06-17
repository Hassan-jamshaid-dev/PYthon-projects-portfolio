# ENCRYPTION PROGRAM

import string
import random
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
print(chars)
print(keys)

plain = input("Enter a message to be encrypted: ")
cipher = ""

for l in plain:
    index = chars.index(l)
    cipher = cipher +keys[index]


print(f"Your original message was {plain}")
print(f"Your encrypted message is {cipher}")


cipher = input("Enter a message to be decrypted: ")
plain = ""

for l in cipher:
    index = keys.index(l)
    plain = plain +chars[index]


print(f"Your encrypted message is {cipher}")
print(f"Your original message was {plain}")