import hashlib


def ctf_function():
	data = b'\x11\x00\x02R+\x1fA\x06\x00\x12O*+hHVF\x10AX\x14'
	key= "how to use XOR"
	print(f"Algo falta aqui...")

def encrypt_bytes():
	data = b'\x11\x00\x02R+\x1fA\x06\x00\x12O*+hHVF\x10AX\x14'
	key= "how to use XOR"
	encrypted = bytearray()
	key_index = 0
	for byte in data:
		encrypted.append(byte ^ ord(key[key_index % len(key)]))
		key_index += 1
	return bytes(encrypted)

def check_password(key):
	password = "fcb3c24dcfc167aa7bb30cd92feb3454cb99b54ebd3291a3a316938012fa0c1b"
	return hashlib.sha256(key.encode()).hexdigest() == password
	

def hidden_flag():
	try:
		path = input(r'Enter path of Image : ')
		password = input('Enter Password for encryption of Image : ')
		if not check_password(password):
			print("Wrong password")
			return
		key = hashlib.sha256(password.encode()).digest()
		with open(path, 'rb') as fin:
			image = fin.read()
		image = bytearray(image)
		key_length = len(key)
		for index, value in enumerate(image):
			image[index] = value ^ key[index % key_length]
		with open(path, 'wb') as fin:
			fin.write(image)
	except Exception as e:
		print(f'Error caught: {e}')

encrpyted = encrypt_bytes()
print(encrpyted)
hidden_flag()
