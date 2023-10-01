import uuid
import hashlib

def random_email():
    email = str(uuid.uuid4()) + "@cevipsa.com"
    hashed_email_address = hashlib.md5(email.encode('utf-8')).hexdigest()
    return [email, hashed_email_address]
