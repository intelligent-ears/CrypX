# utils/matrix.py

from utils.gf import gf_mul

def matrix_mul(state: list, matrix: list, mod_poly=0b10011) -> list:
    """Multiply state vector with matrix in GF"""
    result = []
    for row in matrix:
        res = 0
        for i in range(len(row)):
            res ^= gf_mul(row[i], state[i], mod_poly)
        result.append(res)
    return result

def matrix_mix_columns(state: list, mix_matrix: list, mod_poly=0b10011) -> list:
    """Apply MixColumns on full state"""
    return [matrix_mul(column, mix_matrix, mod_poly) for column in state]

