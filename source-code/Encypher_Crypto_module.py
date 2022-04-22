# PythonCryptoUtility Cryptography module
# made by soules-one
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome.PublicKey import RSA
modern_mods = (AES.MODE_EAX, AES.MODE_SIV, AES.MODE_GCM, AES.MODE_OCB)
classic_modes = (AES.MODE_CBC, AES.MODE_OFB, AES.MODE_CFB)


def str_to_raw(s):
    raw_map = {8:r'\b', 7:r'\a', 12:r'\f', 10:r'\n', 13:r'\r', 9:r'\t', 11:r'\v'}
    return r''.join(i if ord(i) > 32 else raw_map.get(ord(i), i) for i in s)


def mode_selector(a):
    if a == "EAX":
        return AES.MODE_EAX
    elif a == "GCM":
        return AES.MODE_GCM
    elif a == "OCB":
        return AES.MODE_OCB
    elif a == "CBC":
        return AES.MODE_CBC
    else:
        raise ValueError


def p_encrypt(data, key, mode=AES.MODE_CBC):
    cipher = AES.new(key, mode)
    c_data = cipher.encrypt(data)
    return c_data, cipher.iv


def p_encrypt_start(data_name, out_name, par_name="", mode=AES.MODE_CBC, password=""):
    global modern_mods
    global classic_modes
    if mode == AES.MODE_SIV:
        lp = 32
    else:
        lp = 16
    if password == "":
        key = get_random_bytes(lp)
    else:
        if len(password) < lp:
            while len(password) != lp:
                password += " "
        elif len(password) > lp:
            password = password[:lp]
        key = password.encode()
    with open(data_name, "rb") as file:
        data = file.read()
    if mode in (AES.MODE_CBC, AES.MODE_CBC):
        data = pad(data, AES.block_size)
    if mode in classic_modes:
        c_data, iv = p_encrypt(data, key, mode)
        if par_name != "":
            with open(par_name, "wb") as file:
                file.write(iv)
                file.write(key)
    elif mode in modern_mods:
        c_data, nonce, tag, header = p_encrypt_k(data, key, mode)
        if par_name != "":
            with open(par_name, "wb") as file:
                file.write(tag)
                file.write(nonce)
                file.write(key)
                file.write(header)
    else:
        return None
    if par_name == "":
        if mode in modern_mods:
            with open(out_name, "wb") as file:
                file.write(nonce)
                file.write(tag)
                file.write(header)
                file.write(c_data)
            if password == "":
                with open(out_name+"_key.txt", "w") as file:
                    file.write(key)
        if mode in classic_modes:
            with open(out_name, "wb") as file:
                file.write(iv)
                file.write(c_data)
            if password == "":
                with open(out_name+"_key.txt", "w") as file:
                    file.write(key)
    else:
        with open(out_name, 'wb') as file:
            file.write(c_data)


def p_decrypt(key, iv, c_data, mode=AES.MODE_CBC):
    cipher = AES.new(key, mode, iv=iv)
    data = cipher.decrypt(c_data)
    return data


def p_decrypt_start(enc_data_name, out_name, par_name="", mode=AES.MODE_CBC, password=""):
    global modern_mods
    global classic_modes
    if len(password) < 16:
        while len(password) != 16:
            password += " "
    elif len(password) > 16:
        password = password[:16]
    if par_name == "":
        key = password.encode()
        with open(enc_data_name, "rb") as file:
            if mode in modern_mods:
                if mode == AES.MODE_OCB:
                    nonce = file.read(15)
                else:
                    nonce = file.read(16)
                tag = file.read(16)
                header = file.read(128)
                c_data = file.read()
            elif mode in classic_modes:
                iv = file.read(16)
                c_data = file.read()
    else:
        with open(enc_data_name, "rb") as file:
            c_data = file.read()
    if mode in (AES.MODE_EAX, AES.MODE_SIV, AES.MODE_GCM, AES.MODE_OCB):
        if par_name != "":
            with open(par_name, "rb") as file:
                tag = file.read(16)
                if mode == AES.MODE_OCB:
                    nonce = file.read(15)
                else:
                    nonce = file.read(16)
                if mode == AES.MODE_SIV:
                    key = file.read(32)
                else:
                    key = file.read(16)
                header = file.read()
        data = p_decrypt_k(key, tag, nonce, header, c_data, mode)
    else:
        if par_name != "":
            with open(par_name, "rb") as file:
                iv = file.read(16)
                key = file.read(16)
        data = p_decrypt(key, iv, c_data, mode)
    if mode in (AES.MODE_CBC, AES.MODE_CBC):
        data = unpad(data, AES.block_size)
    with open(out_name, "wb") as file:
        file.write(data)


def keys_creation(private_name, public_name, code, size=2048):
    if size < 2048:
        key = RSA.generate(2048)
    else:
        key = RSA.generate(size)
    enc_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
    file = open(private_name + ".pem", "wb")
    file.write(enc_key)
    file.close()
    file = open(public_name + ".pem", "wb")
    file.write(key.publickey().exportKey())
    file.close()


def keys_get_public(private_name, public_name, code):
    with open(private_name, "rb") as file:
        p_key = file.read()
    key = RSA.importKey(p_key, passphrase=code)
    with open(public_name + ".pem", "wb") as file:
        file.write(key.publickey().exportKey())


def p_encrypt_k(data, session_key, mode=AES.MODE_EAX):
    key = session_key
    if mode == AES.MODE_OCB:
        nonce = get_random_bytes(15)
    else:
        nonce = get_random_bytes(16)
    cipher = AES.new(key, mode, nonce)
    header = get_random_bytes(128)
    cipher.update(header)
    c_data, tag = cipher.encrypt_and_digest(data)
    return c_data, nonce, tag, header


def keys_encrypt_aes(data_name, out_name, public_name, mode=AES.MODE_EAX):
    with open(data_name, "rb") as file:
        data = file.read()
    file = open(public_name, "rb")
    public_key = RSA.importKey(file.read())
    if mode == AES.MODE_SIV:
        session_key = get_random_bytes(32)
    else:
        session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    c_data, nonce, tag, header = p_encrypt_k(data, session_key, mode)
    enc_nonce = cipher_rsa.encrypt(nonce)
    with open(out_name, "wb") as file:
        file.write(enc_session_key)
        file.write(enc_nonce)
        file.write(tag)
        file.write(header)
        file.write(c_data)


def p_decrypt_k(key, tag, nonce, header, c_data, mode=AES.MODE_EAX):
    cipher = AES.new(key, mode, nonce)
    cipher.update(header)
    data = cipher.decrypt_and_verify(c_data, tag)
    return data


def keys_decrypt_aes(c_data_name, out_name, key_name, code, mode=AES.MODE_EAX):
    file = open(key_name, "rb")
    private_key = RSA.importKey(file.read(), passphrase=code)
    file.close()
    with open(c_data_name, "rb") as file:
        enc_session_key, enc_nonce, tag, header, c_data = [file.read(i) for i in (private_key.size_in_bytes(),
                                                                                  private_key.size_in_bytes(),
                                                                                  16,
                                                                                  128,
                                                                                  -1)]
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    nonce = cipher_rsa.decrypt(enc_nonce)
    data = p_decrypt_k(session_key, tag, nonce, header, c_data, mode)
    with open(out_name, "wb") as file:
        file.write(data)


def keys_encrypt_rsa(data_name, out_name, public_name):
    with open(data_name, "rb") as file:
        data = file.read()
    file = open(public_name, "rb")
    public_key = RSA.importKey(file.read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    c_data = cipher_rsa.encrypt(data)
    with open(out_name, "wb") as file:
        file.write(c_data)


def keys_decrypt_rsa(c_data_name, out_name, key_name, code):
    file = open(key_name, "rb")
    private_key = RSA.importKey(file.read(), passphrase=code)
    file.close()
    with open(c_data_name, "rb") as file:
        c_data = file.read()
    cipher_rsa = PKCS1_OAEP.new(private_key)
    data = cipher_rsa.decrypt(c_data)
    with open(out_name, "wb") as file:
        file.write(data)


