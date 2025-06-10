import ecdsa
import os

# Ensure the directory for storing keys exists
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Generate a signing key (private key)
        sk = ecdsa.SigningKey.generate()

        # Generate the verifying key (public key)
        vk = sk.get_verifying_key()

        # Write the private key to a file
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        # Write the public key to a file
        with open('cipher/ecc/keys/publickey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Load the private key
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Load the public key
        with open('cipher/ecc/keys/publickey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())

        return sk, vk

    def sign(self, message, key):
        # Sign the message using the private key
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        # Verify the signature using the public key
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False