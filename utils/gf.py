# utils/gf.py

def gf_add(x: int, y: int) -> int:
    return x ^ y  # Addition in GF(2^n) is XOR

def gf_mul(x: int, y: int, mod_poly: int = 0b10011) -> int:
    """Multiply two GF elements modulo a polynomial (default: x^4 + x + 1 for GF(2^4))"""
    result = 0
    while y:
        if y & 1:
            result ^= x
        x <<= 1
        if x & 0x10:  # For GF(2^4), mask = 0x10
            x ^= mod_poly
        y >>= 1
    return result & 0xF  # Mask for GF(2^4)

def gf_pow(x: int, power: int, mod_poly: int = 0b10011) -> int:
    result = 1
    for _ in range(power):
        result = gf_mul(result, x, mod_poly)
    return result

def gf_inv(x: int, mod_poly: int = 0b10011) -> int:
    for i in range(1, 16):
        if gf_mul(x, i, mod_poly) == 1:
            return i
    raise ValueError("No inverse exists")

