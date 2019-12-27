#include <stdio.h>
#include <string.h>
#include "sodium.h"

// Display binary data as hexadecimal strings
void bin_to_hex(unsigned char bin_data[], char hex_data[], int bin_size)
{
    for (int i = 0;  i < bin_size; i++)
    {
        sprintf(&hex_data[i*2], "%02X", bin_data[i]);
    }
}

// Convert hexadecimal data to binary
void hex_to_bin(char hex_data[], unsigned char bin_data[], int bin_size)
{
    char hex_byte_tmp[3];
    for (int i = 0; i < bin_size; i++)
    {
        memcpy(hex_byte_tmp, &hex_data[i*2], 2);
        hex_byte_tmp[2] = '\0';
        bin_data[i] = (int) strtol(hex_byte_tmp, NULL, 16);
    }
}

// Read an input message
int read(char chain[], int length)
{
    char *return_char_position = NULL;
    int tmp = 0;
    if (fgets(chain, length, stdin) != NULL)
    {
        // Try to find a '\n' character.
        // If none is found, reset to the end of the stream.
        return_char_position = strchr(chain, '\n');
        if (return_char_position != NULL)
        {
            *return_char_position = '\0';
        }
        else
        {
            while (tmp != '\n' && tmp != EOF)
            {
                tmp = getchar();
            }
        }
        return 1;
    }
    else
    {
        while (tmp != '\n' && tmp != EOF)
        {
            tmp = getchar();
        }
        return 0;
    }
}

// Encrypt a message given in command line, using secret_key and a randomly
// generated nonce.
void encrypt(unsigned char secret_key[])
{
    // Read the message
    char plain_message[1001];
    puts("Enter the plaintext message (no return, less than 1000 characters)");
    read(plain_message, 1001);

    // Compute the plain and encrypted message size
    unsigned int plain_size = strlen(plain_message);
    unsigned char encrypted_text[plain_size + crypto_secretbox_MACBYTES];

    // Generate a 24 bytes nonce and convert it to a hex string for display
    unsigned char nonce[crypto_secretbox_NONCEBYTES];
    randombytes_buf(nonce, sizeof nonce);
    char nonce_hex[crypto_secretbox_NONCEBYTES * 2 + 1];
    bin_to_hex(nonce, nonce_hex, sizeof nonce);

    // Encrypt the message using the secret key and the nonce
    crypto_secretbox_easy(encrypted_text, plain_message, plain_size, nonce,
        secret_key);
    char encrypted_text_hex[sizeof encrypted_text * 2 + 1];
    bin_to_hex(encrypted_text, encrypted_text_hex, sizeof encrypted_text);

    // Display the pair nonce:encrypted_text
    puts("NONCE: ENCRYPTED TEXT (to copy)");
    printf("%s:%s\n", nonce_hex, encrypted_text_hex);
}

// Decrypt a message given in command line, using secret_key and the nonce
// transmitted alongside the message.
void decrypt(unsigned char secret_key[])
{
    // Read the encrypted message
    char nonce_enctext_couple[1000 + crypto_secretbox_NONCEBYTES + 1 + 
        crypto_secretbox_MACBYTES];
    printf("Enter a couple NONCE: ENCRYPTED TEXT (paste here)\n");
    read((char*) nonce_enctext_couple, 1000);

    // Extract the nonce and convert it to binary
    unsigned char nonce_bin[crypto_secretbox_NONCEBYTES];
    hex_to_bin(nonce_enctext_couple, nonce_bin, crypto_box_NONCEBYTES);

    // Extract the encrypted text and convert it to binary
    int idx_start_enctext = crypto_secretbox_NONCEBYTES * 2 + 1;
    int size_enctext = strlen(nonce_enctext_couple) - idx_start_enctext;
    unsigned char encrypted_text_bin[size_enctext / 2];
    hex_to_bin(&nonce_enctext_couple[idx_start_enctext], encrypted_text_bin, 
        sizeof encrypted_text_bin);

    // Decrypt the encrypted text using the secret key and the nonce.
    // The plaintext message size is the same as the encrypted one, minus the
    // MAC code size, plus 1 final NULL character.
    char plain_messsage[sizeof encrypted_text_bin
        - crypto_secretbox_MACBYTES + 1];
    if (crypto_secretbox_open_easy(plain_messsage, encrypted_text_bin,
        sizeof encrypted_text_bin, nonce_bin, secret_key) != 0)
    {
        puts("Error encoutered during decryption - invalid secret key, nonce or encrypted text");
    }
    plain_messsage[sizeof plain_messsage - 1] = '\0';

    // Display the decrypted message
    puts("Decrypted message:");
    puts(plain_messsage);
}

// Encrypt a message given in command line, using the AES-GCM algorithm with a
// secret_key and a counter nonce.
void encrypt_AES_GCM(unsigned char secret_key[], unsigned char nonce[])
{
    // Read the message
    char plain_message[1001];
    puts("Enter the plaintext message (no return, less than 1000 characters)");
    read(plain_message, 1001);

    // Compute the plain and encrypted message size
    unsigned int plain_size = strlen(plain_message);
    unsigned char encrypted_text[plain_size + crypto_aead_aes256gcm_ABYTES];

    // Use the nonce as a counter
    unsigned char nonce_initial[crypto_aead_aes256gcm_NPUBBYTES] = {0};
    sodium_increment(nonce, crypto_aead_aes256gcm_NPUBBYTES);
    if (sodium_compare(nonce, nonce_initial, crypto_aead_aes256gcm_NPUBBYTES) 
        == 0)
    {
        puts("You have exhausted all possible nonces with this key");
        return;
    }
    char nonce_hex[crypto_aead_aes256gcm_NPUBBYTES * 2 + 1];
    bin_to_hex(nonce, nonce_hex, crypto_aead_aes256gcm_NPUBBYTES);

    // Encrypt message using key and nonce, and store it in cyphertext buffer
    crypto_aead_aes256gcm_encrypt(encrypted_text, NULL, plain_message, 
        plain_size, NULL, NULL, NULL, nonce, secret_key);
    char encrypted_text_hex[sizeof encrypted_text * 2 + 1];
    bin_to_hex(encrypted_text, encrypted_text_hex, sizeof encrypted_text);

    // Display the pair nonce:encrypted_text
    puts("NONCE: ENCRYPTED TEXT (to copy)");
    printf("%s:%s\n", nonce_hex, encrypted_text_hex);
}

// Decrypt a message given in command line, using the AES-GCM algorithm with a
// secret_key and the nonce transmitted alongside the message.
void decrypt_AES_GCM(unsigned char secret_key[])
{
    // Read the encrypted message
    char nonce_enctext_couple[1000 + crypto_aead_aes256gcm_NPUBBYTES + 1 + 
        crypto_aead_aes256gcm_ABYTES];
    printf("Enter a couple NONCE: ENCRYPTED TEXT (paste here)\n");
    read(nonce_enctext_couple, 1000);

    // Extract the nonce and convert it to binary
    unsigned char nonce_bin[crypto_aead_aes256gcm_NPUBBYTES];
    hex_to_bin(nonce_enctext_couple, nonce_bin,
        crypto_aead_aes256gcm_NPUBBYTES);

    // Extract the encrypted text and convert it to binary
    int idx_start_enctext = crypto_aead_aes256gcm_NPUBBYTES * 2 + 1;
    int size_enctext = strlen(nonce_enctext_couple) - idx_start_enctext;
    unsigned char encrypted_text_bin[size_enctext / 2];
    hex_to_bin(&nonce_enctext_couple[idx_start_enctext], encrypted_text_bin, 
        sizeof encrypted_text_bin);

    // Decrypt the encrypted text using the secret key and the nonce.
    // The plaintext message size is the same as the encrypted one, minus the
    // MAC code size, plus 1 final NULL character.
    char plain_messsage[sizeof encrypted_text_bin
        - crypto_aead_aes256gcm_ABYTES + 1];
    if (crypto_aead_aes256gcm_decrypt(plain_messsage, NULL, NULL, 
        encrypted_text_bin, sizeof encrypted_text_bin, NULL, NULL, nonce_bin, 
        secret_key) != 0)
    {
        puts("Error encoutered during decryption - invalid secret key, nonce or encrypted text");
    }
    plain_messsage[sizeof plain_messsage - 1] = '\0';

    // Display the decrypted message
    puts("Decrypted message:");
    puts(plain_messsage);
}

int main(void)
{
    // Initialize libsodium
    if (sodium_init() < 0)
    {
        puts("Error - Could not initialize libsodium library");
        return EXIT_FAILURE;
    }

    // // Generate a 32 bytes key, using libsodium's cryptographic GNPA
    // unsigned char secret_key[crypto_secretbox_KEYBYTES];
    // randombytes_buf(secret_key, crypto_secretbox_KEYBYTES);

    // Generate a 32 bytes master key, using libsodium's cryptographic GNPA.
    // Using the same key for secretbox and AES-GCM is indeed unsafe.
    unsigned char master_key[crypto_kdf_KEYBYTES];
    unsigned char secret_key_secretbox[crypto_secretbox_KEYBYTES];
    unsigned char secret_key_AES_GCM[crypto_aead_aes256gcm_KEYBYTES];

    randombytes_buf(master_key, crypto_kdf_KEYBYTES);
    crypto_kdf_derive_from_key(secret_key_secretbox, sizeof 
        secret_key_secretbox, 1, "CONTEXT_", master_key);
    crypto_kdf_derive_from_key(secret_key_AES_GCM, sizeof 
        secret_key_AES_GCM, 2, "CONTEXT_", master_key);

    // Generate the AES-GCM nonce, initialized to 0 everywhere.
    // Due to its smaller size of 96 bits, it is unsecure to generate it
    // randomly (high risk of collision), so we treat it as a counter.
    unsigned char nonce_AES_GCM[crypto_aead_aes256gcm_NPUBBYTES] = {0};

    // Command line menu
    char choice[2];
    int int_choice;

    do
    {
        int_choice = -1;
        puts("");
		puts("Symmetric encryption -- Menu: \n");
		puts("1. Encrypt a message");
		puts("2. Decrypt a message");
		puts("3. Encrypt a message using AES-GCM");
		puts("4. Decrypt a message using AES-GCM");
		puts("0. Exit the program");
        read(choice, 2);

        sscanf(choice, "%d", &int_choice);
        switch (int_choice)
        {
        case 1:
            encrypt(secret_key_secretbox);
            break;
        case 2:
            decrypt(secret_key_secretbox);
            break;
        case 3:
            encrypt_AES_GCM(secret_key_AES_GCM, nonce_AES_GCM);
            break;
        case 4:
            decrypt_AES_GCM(secret_key_AES_GCM);
            break;
        case 0:
            break;
        
        default:
            printf("Error - unknown command %s", choice);
            break;
        }
    } while (int_choice != 0);
    
    return EXIT_SUCCESS;
}