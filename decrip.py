import os
import pyaes

## abrir arquivo

file_name = "msg.txt.troll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para decriptografia

key = b"teste12345678901"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo  criptografado

os.remove(file_name)

# criar o arquivo descriptografado

new_file = "msg.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()

