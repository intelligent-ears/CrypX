# attacks/linear.py

import numpy as np
from core.interfaces import Attack, AttackResult
from utils.sbox import compute_lat
import matplotlib.pyplot as plt

class LinearAttackResult(AttackResult):
    def __init__(self, lat, max_bias, input_mask, output_mask):
        self.lat = lat
        self.max_bias = max_bias
        self.in_mask = input_mask
        self.out_mask = output_mask

    def summary(self):
        return (f"Max linear bias: {self.max_bias:.4f} for input_mask=0x{self.in_mask:X}, "
                f"output_mask=0x{self.out_mask:X}")

    def to_dict(self):
        return {
            "max_bias": self.max_bias,
            "input_mask": self.in_mask,
            "output_mask": self.out_mask,
            "lat": self.lat.tolist()
        }

    def visualize(self):
        plt.imshow(np.abs(self.lat), cmap='OrRd')
        plt.title("Linear Approximation Table (LAT)")
        plt.xlabel("Output Mask")
        plt.ylabel("Input Mask")
        plt.colorbar()
        plt.show()

class LinearAttack(Attack):
    def __init__(self, cipher):
        self.cipher = cipher

    def run(self, **kwargs) -> AttackResult:
        sbox = self.cipher.get_sbox()
        lat = compute_lat(sbox)
        max_bias = np.max(np.abs(lat[1:]) / 16)  # ignore first row
        in_mask, out_mask = np.unravel_index(np.argmax(np.abs(lat)), lat.shape)
        return LinearAttackResult(lat, max_bias, in_mask, out_mask)
