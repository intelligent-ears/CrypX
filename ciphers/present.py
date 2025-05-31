from core.interfaces import Cipher

SBOX = [
    0xC, 0x5, 0x6, 0xB,
    0x9, 0x0, 0xA, 0xD,
    0x3, 0xE, 0xF, 0x8,
    0x4, 0x7, 0x1, 0x2
]

INV_SBOX = [SBOX.index(i) for i in range(16)]

PBOX = [0, 16, 32, 48, 1, 17, 33, 49,
        2, 18, 34, 50, 3, 19, 35, 51,
        4, 20, 36, 52, 5, 21, 37, 53,
        6, 22, 38, 54, 7, 23, 39, 55,
        8, 24, 40, 56, 9, 25, 41, 57,
        10, 26, 42, 58, 11, 27, 43, 59,
        12, 28, 44, 60, 13, 29, 45, 61,
        14, 30, 46, 62, 15, 31, 47, 63]

class PRESENT(Cipher):
    def __init__(self):
        self.rounds = 5 
        self.sbox = SBOX
        self.inv_sbox = INV_SBOX
        self.pbox = PBOX

    def block_size(self) -> int:
        return 64

    def key_size(self) -> int:
        return 80

    def get_sbox(self) -> list:
        return self.sbox

    def encrypt(self, plaintext: bytes, key: bytes) -> bytes:
        state = int.from_bytes(plaintext, 'big')
        round_key = int.from_bytes(key, 'big')

        for r in range(self.rounds):
            state ^= (round_key >> 16) & 0xFFFFFFFFFFFFFFFF 
            state = self._substitute(state)
            state = self._permute(state)
            round_key = self._update_key(round_key, r)

        state ^= (round_key >> 16) & 0xFFFFFFFFFFFFFFFF
        return state.to_bytes(8, 'big')

    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        raise NotImplementedError("Decryption not implemented for PRESENT (toy version)")

    def _substitute(self, state: int) -> int:
        output = 0
        for i in range(16):
            nibble = (state >> (i * 4)) & 0xF
            output |= self.sbox[nibble] << (i * 4)
        return output

    def _permute(self, state: int) -> int:
        output = 0
        for i in range(64):
            bit = (state >> i) & 1
            output |= bit << self.pbox[i]
        return output

    def _update_key(self, key: int, round: int) -> int:
        key = ((key << 61) | (key >> 19)) & ((1 << 80) - 1)

        sbox_in = (key >> 76) & 0xF
        key = (key & ~(0xF << 76)) | (self.sbox[sbox_in] << 76)

        key ^= round << 15
        return key

