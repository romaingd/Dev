import nacl.pwhash

# Plain password
plain_password = b"my1Password"

# Generate the password hash using Argon2. The hash contains a randomly generated salt and can be safely stored in a database.
hashed_password = nacl.pwhash.str(plain_password)

# Verify the password, using the salt that is stored with the hash. This is done by hashing the given password with the same salt, and comparing with the hash stored in database in constant time, to prevent timing attacks.
if nacl.pwhash.verify(hashed_password, plain_password):
    print("Valid password")
else:
    print("Invalid password")