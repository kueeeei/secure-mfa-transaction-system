# MFA Transaction based on QR-code (Crypto Part)
## What is this about?
This repo includes crypto part of a MFA transaction system project. 
This project is designed with 3 main components:
- Web app (Online Shopping Website)
- Bank App
- Bank Server
The main point of this project is providing a secure payment. We reached this goal by using RSA Cipher and RSA signature.

## How it works?
While Web user clicks payment button from Web app, Bank Server will generates a QR-code embeded with encrypted transaction information for web users to scan. After registered in Bank app, users are allowed to scan QR code with Bank app and approve or reject the transaction. After approving transaction requirement, Bank server side can verify the approval by the RSA signature. This transaction will only succesed when the requirement is approved on bank app and verified the approval is made by the Bank account owner.

## Cryptography Concepts
In this project, my duty is the crypto part. The implementation involves two concepts.
1. RSA Cipher  
    - Key Generation
        Public key and private key generation occurs when user registered from bank app. Public key will be sent back to server and saved in database, while private key will be stored in device secure space directly.
    - Encryption
        The transaction info will be encrypted with public key. 
        | C = M ^ e mod n
    - Decryption
        After scan and get cipher text from QR-code, bank app will access private key and decrypt the ciphertext with it.
        | M = C ^ d mod n
2. RSA Signature
    Before the encryption, server side generates a hash digest of transaction information and saves in database. The Hash method used here is SHA256. After transaction approved from bank app, app generates a digest with same measure and signs with user private key. Once server received this sign, it decrypts the sign with public key and compares the hash digest with the origin saved one.

## Advantage of This Design
- Authenticity and Integrity
RSA cipher ensure the secure of sensitive information, since the ciphertext can be decrypted only with the correct private key. RSA signature allows bank server checks whether account owner approved with the right information.





