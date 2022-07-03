import binascii
from hashlib import sha3_512
import random

genesis_block = bytearray([0 for i in range(0, 64)])
base_block = genesis_block


def random_block(limit):
    for i in range(0, limit):
        ml = sha3_512()
        ml.update(str(random.randint(0, 1e18)).encode("iso-8859-1"))
        yield bytearray(ml.hexdigest().encode("iso-8859-1"))


def signed_block(baseblock, limit):
    for block in random_block(limit):
        block_data = baseblock + block
        digest = sha3_512()
        digest.update(block_data)
        baseblock = digest.digest()
        yield block_data + digest.digest()


limit = 3
blocks = [block for block in signed_block(genesis_block, limit)]
assert len(blocks) == limit
for block in blocks:
    print("link=" + binascii.hexlify(block[0:64]).decode("iso-8859-1"))
    print("data=" + block[64:192].decode("iso-8859-1"))
    print("digest=" + binascii.hexlify(block[192:256]).decode("iso-8859-1"))
    print("==========================")
    assert(len(block) == 256)
