from hashlib import md5, sha256

# obj = md5()
salt = b"jkhjdskfhkrwerewrw"
obj = md5(salt)  # 加盐

obj.update(b"123456")
print(obj.hexdigest())

# obj2 = sha256()
obj2 = sha256(salt)  # 加盐

obj2.update(b"123456")
print(obj2.hexdigest())
