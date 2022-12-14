def make_block(lst):
    return (ord(lst[0])<<24) + (ord(lst[1])<<16) + (ord(lst[2])<<8) + ord(lst[3])

def encrypt(message, key):
    rv = ""
    l = list(message)
    n = len(message)
    blocks = []
    for i in range(0,n,4):# break message into 4-character blocks
        if i+4 <= n:
            blocks.append(make_block(l[i: i+4]))
        else:# pad end of message with white-space if the lenght is not divisible by 4
            end = l[i:n]
            end.extend((i+4-n)*[' '])
            blocks.append(make_block(end))
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    for block in blocks:#encrypt each  block separately
        encrypted = str(hex(block ^ extended_key))[2:]
        for i in range(8 - len(encrypted)):
            rv += '0'
        rv += encrypted
    return rv

def decrypt(message, key):
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    msg = ""
    for i in range(0, len(message), 8):
        conv = int(message[i:i + 8], 16) ^ extended_key
        t1 = chr(conv // 2 ** 24)
        conv -= ord(t1) << 24
        t2 = chr(conv // 2 ** 16)
        conv -= ord(t2) << 16
        t3 = chr(conv // 2 ** 8)
        conv -= ord(t3) << 8
        t4 = chr(conv)
        msg += t1 + t2 + t3 + t4
    print ("plz meaningful English word: ", msg)


decrypt("10170d1c0b17180d10161718151003180d101617",121)
