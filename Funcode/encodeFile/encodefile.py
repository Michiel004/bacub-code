import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import struct



class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()
        

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

 



#output = my_AESCipher.decrypt(secret)
#print(output)

'''
secret = my_AESCipher.encrypt("this is private")

with open("secret.txt", "w") as myfile:
    myfile.write(str(secret))

'''

with open('secret.txt') as f:
    secretTekst = f.readlines()
my_AESCipher = AESCipher("test")
whatTypIsThis = my_AESCipher.encrypt("geheim")
print(type(whatTypIsThis))
#print(str(secretTekst))
mystringtest = b'JXlgt5uPeSIlzTiBDvRpVjkycJkwNJXTc+2CGs6zqGr0mRlSBBg7yZ5F4jYXuVuw',dnfdnf,dn"
my_str_as_bytes = mystringtest.encode('utf-8')




output = my_AESCipher.decrypt(y)
'''
output = my_AESCipher.decrypt(secretTekst)
print(str(output))
'''