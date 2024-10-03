def	count_char(array):
	return(len(array))
def leer_array_mixto_binario(array):
    resultado_binario = ''
    for elemento in array:
        # Si el elemento es un entero (hexadecimal), lo convertimos a su carácter y luego a binario
        if isinstance(elemento, int):
            caracter = chr(elemento)
        else:
            caracter = elemento
        # Convertimos el carácter a binario y lo unimos al resultado
        resultado_binario += format(ord(caracter), '08b') + ' '
    
    return resultado_binario.strip()  # Elimina el último espacio extra

def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:]

def encrypt_bytes(data, key):
    encrypted = ""
    key_index = 0
    
    for byte in data:
        # XOR el byte actual con el siguiente carácter de la clave
        encrypted += chr(byte ^ ord(key[key_index % len(key)]))
        
        # Avanza al siguiente carácter de la clave
        key_index += 1
    
    return encrypted.encode('utf-8')

def menu(array):
	print("-----------------------------------------")
	print(f"\t\tCTF XOR SOLVER\n")
	print(f"\t\t\tby:FamilyBoggart")
	print("-----------------------------------------\n")
	print(f"Tu flag original es: {array}\n")
	print("OPCIONES:")
	print("1) Hacer XOR con formato: ctf{flag}")
	print("2) Hacer XOR con formato: CTF{flag}")
	print("3) Mostrar cadena en binario")
	print("")
	option = int(input("Selecciona tu opcion: "))
	if option == 1:
		flag = descifrar_xor(array,"ctf")
		print(f"\nLa flag podria ser: {flag}")
	elif option == 2:
		flag = descifrar_xor(array,"CTF")
		print(f"\nLa flag podria ser: {flag}")
	elif option == 3:
		txt = leer_array_mixto_binario(array)
		print(f"\nTu cadena en binario es la siguiente:\n{txt}")
	print("")
	again = input("¿DESEAS HACER ALGO MAS? (Y/N)")
	if again == 'Y':
		menu(array)
	else:
		print("Bye!!")






# Ejemplo de uso
array_input = ['\x00', '\x00', '\x00', '\x18', 'C', '_', '\x05', 'E', 'V', 'T', 'F', 'U', 'R', 'B', '_', 'U', 'G', '_', 'V', '\x17', 'V', 'S', '@', '\x03', '[', 'C', '\x02', '\x07', 'C', 'Q', 'S', 'M', '\x02', 'P', 'M', '_', 'S', '\x12', 'V', '\x07', 'B', 'V', 'Q', '\x15', 'S', 'T', '\x11', '_', '\x05', 'A', 'P', '\x02', '\x17', 'R', 'Q', 'L', '\x04', 'P', 'E', 'W', 'P', 'L', '\x04', '\x07', '\x15', 'T', 'V', 'L', '\x1b']
binario = leer_array_mixto_binario(array_input)


def descifrar_xor(xored, known_flag_start):
    """
    Función que descifra una lista de caracteres XORed utilizando una suposición de la clave.
    
    :param xored: Lista de caracteres XORed.
    :param known_flag_start: Parte conocida de la flag (ej. "CTF{").
    :return: La flag descifrada.
    """
    # Convertimos los caracteres conocidos en sus códigos ASCII
    known_flag_start_ascii = [ord(c) for c in known_flag_start]

    # Extraemos los primeros caracteres de la lista XORed para calcular la clave
    xored_start_ascii = [ord(c) for c in xored[:len(known_flag_start)]]

    # Calculamos la clave XOR para los primeros caracteres
    key = [a ^ b for a, b in zip(known_flag_start_ascii, xored_start_ascii)]

    # Duplicamos la clave hasta cubrir la longitud completa del mensaje XORed
    key_repeated = key * (len(xored) // len(key)) + key[:len(xored) % len(key)]

    # Realizamos la operación XOR completa para descifrar el mensaje
    decrypted_message = ''.join([chr(ord(c) ^ k) for c, k in zip(xored, key_repeated)])

    # Retornamos el mensaje descifrado
    return decrypted_message

menu(array_input)
