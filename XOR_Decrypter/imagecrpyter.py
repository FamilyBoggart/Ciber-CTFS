import hashlib

try:
    path = input(r'Enter path of Image : ')
    password = input('Enter Password for encryption of Image : ')
    
    # Convertimos la contraseña en bytes utilizando un hash (SHA-256 en este caso)
    key = hashlib.sha256(password.encode()).digest()
     
    # Abrimos la imagen para lectura en binario
    with open(path, 'rb') as fin:
        image = fin.read()

    # Convertimos la imagen en un array de bytes
    image = bytearray(image)
 
    # Realizamos la operación XOR entre cada byte de la imagen y la clave
    key_length = len(key)
    for index, value in enumerate(image):
        image[index] = value ^ key[index % key_length]
 
    # Abrimos el archivo para escritura en binario y guardamos la imagen cifrada
    with open(path, 'wb') as fin:
        fin.write(image)

    print('Encryption/Decryption Done...')

except Exception as e:
    print(f'Error caught: {e}')
