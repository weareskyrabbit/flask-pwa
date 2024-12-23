import base64
import ecdsa

def generate_vapid_keypair():
    pk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
    vk = pk.get_verifying_key()

    return {
        'private_key': base64.urlsafe_b64encode(pk.to_string()).strip(b"="),
        'public_key': base64.urlsafe_b64encode(b"\x04" + vk.to_string()).strip(b"=")
    }

keypair = generate_vapid_keypair()

print(f"VAPID_PRIVATE_KEY = \'{keypair['private_key'].decode('utf-8')}\'")
print(f"VAPID_PUBLIC_KEY  = \'{keypair['public_key']}\'")