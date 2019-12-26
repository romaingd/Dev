import nacl.utils
from nacl.secret import SecretBox

# Plaintext message
plain_message = b"Hello world"
print("Plain:", plain_message)

# Generate the secret key
secret_key = nacl.utils.random(SecretBox.KEY_SIZE)
print("S key:", secret_key.hex())

# Generate the nonce
nonce = nacl.utils.random(SecretBox.NONCE_SIZE)
print("Nonce:", nonce.hex())

# Encrypt the message
encrypted_message = SecretBox(secret_key).encrypt(plain_message, nonce)
print("Encr.:", encrypted_message.hex())

# Decrypt the message
decrypted_message = SecretBox(secret_key).decrypt(encrypted_message)
print("Decr.:", decrypted_message)