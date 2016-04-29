from simplecrypt import encrypt, decrypt

p = [
'9XB8nsIqRfYeswC', 
'4sEhUGLEZti9BiN', 
'bDjmT0NcIW8nzhb', 
'ZN6QQoMOO1ZQLUY', 
'RVrF2qdMpoq6Lib', 
'tnnX7HH3vJ9Hiji', 
'C24TJYYkqekv40l', 
'B2ropluPaMAitzE', 
'DRezNUVnr2zC0CP', 
'XCNmpTvvZb1n3mX' 
]

with open('encrypted.bin', 'rb') as inp:
	encrypted = inp.read()
	# print(encrypted)

	for x in p:
		# print(x)
		x = x.strip()
		try:
			plaintext = decrypt(x, encrypted)
			print(plaintext)
			print('---------------------')
		except :
			continue
		
	inp.close()