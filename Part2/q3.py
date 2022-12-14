import hashlib
# given message and signature
(n, e) = (0x97987cc9520bf98c049dd4fdd0b2ef50a8cd876bc89b3f43708a8d26e05a2923a312688cd2a50d8e01fa3e20181387d07e9b75d00ad07b2e302983cf16b56bb4dbeeeb2709a22053c44fc743abcac8fc8511b97062ac8c298feeebce70c6851a6752b4f27a8a0fbdd3b202e3e10ea48a912d31f96ecb7bf8fe86934a9b466b71,
0x10001)
signature = (0x230e2ee7c95e6c1faae818682fa25f19d3148077de82a30c44618f397fb0309fc4fe545e6cda6c46dbe81aea4ad76cf3c6ed5066df1a6b1f187063d6cb3f8da69675e91cb9ffea6a79814bd27153f04cfd143d519f8ce0025cc1205c2472294343f14a2d041ddc3821359638638a96d58e6b99a904f6099eea9c74012dd64569)
message = "Your checking account available balance is 12,617,290 dollars and 56 cents."
diffmessage = "Your checking account available balance is 14,545,360 dollars and 69 cents."


# given code

def rsa_message_sign(message: str, d: int, n: int) -> int:
    digest = hashlib.sha256(message.encode("ascii", "ignore"))
    return pow(int(digest.hexdigest(), 16), d, n)

# more given
def rsa_signature_verify(message: str, signature: int, e: int, n: int) -> bool:
    expected_digest = pow(signature, e, n)
    digest = int(hashlib.sha256(message.encode("ascii", "ignore")).hexdigest(), 16)
    return expected_digest == digest

# verify if bob is the sender or not
def verify_sender(incoming: str):
    incoming_ver = rsa_signature_verify(incoming, signature, e, n)
    if (incoming_ver):
        print("Verified")
    else:
        print("Not verified")
# find Bob's genuine signature
def genuine_signature():
    diffmessage_signature = rsa_message_sign(diffmessage, e, n)
    print(diffmessage_signature)

verify_sender(message)
verify_sender(diffmessage)
print("Bob's signature")
genuine_signature()
