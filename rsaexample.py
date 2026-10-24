from cryptography.hazmat.primitives.asymmetric import padding ,rsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Step1 : Generate the issuers RSA key pair

private_key=rsa.generate_private_key(public_exponent=65537,key_size=2048)

public_key=private_key.public_key()
