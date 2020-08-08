#!/usr/bin/python3

import hashlib

hash_value = input("[*] Enter the string to be hashed: ")
hashobj_md5 = hashlib.md5()
hashobj_md5.update(hash_value.encode())
print("MD5: "+hashobj_md5.hexdigest())

hashobj_sha1 = hashlib.sha1()
hashobj_sha1.update(hash_value.encode())
print("SHA-1: " + hashobj_sha1.hexdigest())

hashobj_sha224 = hashlib.sha224()
hashobj_sha224.update(hash_value.encode())
print("SHA-224: " + hashobj_sha224.hexdigest())

hashobj_sha256 = hashlib.sha256()
hashobj_sha256.update(hash_value.encode())
print("SHA-256: " + hashobj_sha256.hexdigest())

hashobj_sha512 = hashlib.sha512()
hashobj_sha512.update(hash_value.encode())
print("SHA-512: " + hashobj_sha512.hexdigest())


