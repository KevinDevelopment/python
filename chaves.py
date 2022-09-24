from pki_helpers import *
private_key = generate_private_key("ca-private-key.pem", "secret_password")

generate_public_key(
private_key,
filename="ca-public-key.pem",
country="US",
state="Maryland",
locality="Baltimore",
org="My CA Company",
hostname="my-ca.com",
)
