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

int main(void)
{
    // Initialize libsodium
    if (sodium_init() < 0)
    {
        puts("Error - Could not initialize libsodium library");
        return EXIT_FAILURE;
    }

    // Generate a 32 bytes key, then use libsodium's cryptographic GNPA
    unsigned char secret_key[crypto_secretbox_KEYBYTES];
    randombytes_buf(secret_key, crypto_secretbox_KEYBYTES);

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
            encrypt(secret_key);
            break;
        case 2:
            // decrypt(secret_key)
            break;
        case 3:
            // encrypt_AES_GCM(secret_key, nonce_AES_GCM)
            break;
        case 4:
            // decrypt_AES_GCM(secret_key, nonce_AES_GCM)
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