import hashlib

string = input("Enter a string: ")

encoded_string = string.encode('utf-8')

md5_hash = hashlib.md5(encoded_string).hexdigest()
sha1_hash = hashlib.sha1(encoded_string).hexdigest()
sha256_hash = hashlib.sha256(encoded_string).hexdigest()

print("MD5: ", md5_hash)
print("SHA1: ", sha1_hash)
print("SHA256: ", sha256_hash)
