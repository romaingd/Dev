import nacl.utils
import nacl.signing

# Generate a public/private (= verify/signing) key pair
signing_key_Alice = nacl.signing.SigningKey(seed=nacl.utils.random())
verify_key_Alice = signing_key_Alice.verify_key

# Sign a message. The result contains both the message and the signature, hence canbe sent as is.
message = b"This message is not confidential, but it is signed by Alice"
signed_message = signing_key_Alice.sign(message)

# Verify the message
original_message = verify_key_Alice.verify(signed_message)
if original_message:
    print(original_message)
