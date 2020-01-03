import string


alpha = string.ascii_lowercase


#abcdefghijklmnopqrstuvwxyz

def encrypt(msg):
	result = ""
	for i in range(0,len(msg)):
		for j in range(0,len(alpha)):
			if msg[i] == alpha[j]:
				result += alpha[-j-1]

	return result
				

print(encrypt("hello my name is kandy"))
print(encrypt("svoolnbmznvrhpzmwb"))