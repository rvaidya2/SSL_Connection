from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import datetime

from cryptography.hazmat.backends import default_backend


private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u'US'),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u'California'),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u'San Francisco'),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u'My Organization'),
    x509.NameAttribute(NameOID.COMMON_NAME, u'myserver.com'),
])

# Create a certificate valid for 365 days
valid_from = datetime.datetime.utcnow()
valid_to = valid_from + datetime.timedelta(days=365)
builder = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    valid_from
).not_valid_after(
    valid_to
)

# Add key usage extension
builder = builder.add_extension(
    x509.KeyUsage(
        digital_signature=True,
        key_encipherment=True,
        key_agreement=False,
        content_commitment=False,
        data_encipherment=False,
        key_cert_sign=False,
        crl_sign=False,
        encipher_only=False,
        decipher_only=False
    ),
    critical=False
)

# Sign the certificate with the private key
certificate = builder.sign(
    private_key=private_key, algorithm=hashes.SHA256(),
    backend=default_backend()
)

# Save the private key and certificate to files
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("certificate.pem", "wb") as cert_file:
    cert_file.write(certificate.public_bytes(encoding=serialization.Encoding.PEM))
