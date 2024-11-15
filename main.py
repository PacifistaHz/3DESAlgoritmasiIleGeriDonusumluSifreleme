from Cryptodome.Cipher import DES3
import base64

BS = DES3.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def sifrele(text, key):
    text = pad(text)
    cipher = DES3.new(key, DES3.MODE_ECB)
    m = cipher.encrypt(text.encode('utf-8'))
    m = base64.b64encode(m)
    return m.decode('utf-8')

def coz(encrypted_text, key):
    encrypted_text = base64.b64decode(encrypted_text)
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(encrypted_text).decode('utf-8'))
    return decrypted_text

# Örnek Kullanım
key = b'Sixteen byte key'
metin = input("Şifrelenmesi istenilen metin: ")
sifreli_metin = sifrele(metin, key)
print("Şifreli Metin:\n" + sifreli_metin)

cozulmus_metin = coz(sifreli_metin, key)
print("Çözülen Metin:\n" + cozulmus_metin)

