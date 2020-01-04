import nacl.pwhash
import nacl.utils
from nacl.secret import SecretBox


# Define global elements
stored_pw = None
secret_key = nacl.utils.random(size=SecretBox.KEY_SIZE)
secret_box = SecretBox(secret_key)


# Define useful functions
def store_password(plain_pw):
    global stored_pw, secret_box
    hashed_pw = nacl.pwhash.str(plain_pw)
    stored_pw = secret_box.encrypt(hashed_pw)
    return


def verify_password(candidate_pw):
    global stored_pw, secret_box
    hashed_stored_pw = secret_box.decrypt(stored_pw)
    try:
        verif_result = nacl.pwhash.verify(hashed_stored_pw, candidate_pw)
    except:
        verif_result = False
    return verif_result


def test_verify_password(candidate_pw):
    if verify_password(candidate_pw):
        print("Valid password")
    else:
        print("Invalid password")
    return


def change_password(new_pw):
    # Check that the new password is not the old password + 1 character
    if verify_password(new_pw[:-1]):
        print("Please use a more substantial change")
        return

    store_password(new_pw)
    print("Password changed")
    return


# Test everything
if __name__ == "__main__":
    store_password(b"my_password")

    print("Correct password accepted:")
    test_verify_password(b"my_password")

    print("Incorrect password rejected:")
    test_verify_password(b"another_pw")

    print("Can change password:")
    change_password(b"another_pw")

    print("Correct new password accepted:")
    test_verify_password(b"another_pw")

    print("Incorrect password change")
    change_password(b"another_pw1")
