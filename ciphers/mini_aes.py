from core.interfaces import Cipher

SBOX = [0x6, 0x4, 0xC, 0x5,
        0x0, 0x7, 0x2, 0xE,
        0x1, 0xF, 0x3, 0xD,
        0x8, 0xA, 0x9, 0xB]

INV_SBOX = [SBOX.index(i) for i in range(16)]

class MiniAES(Cipher):
    def __init__(self):
        self._sbox = SBOX
        self._inv_sbox = INV_SBOX

    def block_size(self) -> int:
        return 16 

    def key_size(self) -> int:
        return 16  

    def get_sbox(self) -> list:
        return self._sbox

    def encrypt(self, plaintext: bytes, key: bytes) -> bytes:
        pt = int.from_bytes(plaintext, byteorder='big')
        k = int.from_bytes(key, byteorder='big')

        state = pt ^ k

        state = self._sub_nibbles(state)

        state = ((state & 0xF000) >> 12) | \
                ((state & 0x0F00) >> 4)  | \
                ((state & 0x00F0) << 4)  | \
                ((state & 0x000F) << 12)

        state ^= k

        return state.to_bytes(2, byteorder='big')

    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        ct = int.from_bytes(ciphertext, byteorder='big')
        k = int.from_bytes(key, byteorder='big')

        state = ct ^ k

        state = ((state & 0xF000) >> 12) | \
                ((state & 0x0F00) >> 4)  | \
                ((state & 0x00F0) << 4)  | \
                ((state & 0x000F) << 12)

        state = self._sub_nibbles(state, inverse=True)

        state ^= k

        return state.to_bytes(2, byteorder='big')

    def _sub_nibbles(self, state: int, inverse=False) -> int:
        box = self._inv_sbox if inverse else self._sbox
        result = 0
        for i in range(4):
            nibble = (state >> (i * 4)) & 0xF
            result |= box[nibble] << (i * 4)
        return result

