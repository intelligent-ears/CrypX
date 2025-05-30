# utils/sbox.py

import numpy as np

def compute_ddt(sbox: list) -> np.ndarray:
    size = len(sbox)
    ddt = np.zeros((size, size), dtype=int)
    for x1 in range(size):
        for dx in range(size):
            x2 = x1 ^ dx
            dy = sbox[x1] ^ sbox[x2]
            ddt[dx][dy] += 1
    return ddt

def compute_lat(sbox: list) -> np.ndarray:
    size = len(sbox)
    lat = np.zeros((size, size), dtype=int)
    for a in range(size):
        for b in range(size):
            total = 0
            for x in range(size):
                in_mask = parity(a & x)
                out_mask = parity(b & sbox[x])
                if in_mask == out_mask:
                    total += 1
                else:
                    total -= 1
            lat[a][b] = total
    return lat

def parity(x: int) -> int:
    return bin(x).count('1') % 2

def invert_sbox(sbox: list) -> list:
    inv = [0] * len(sbox)
    for i, val in enumerate(sbox):
        inv[val] = i
    return inv

