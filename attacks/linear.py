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
        return (f"Max linear bias: {self.max_bias:.4f} "
                f"for input_mask=0x{self.in_mask:X}, output_mask=0x{self.out_mask:X}")

    def to_dict(self):
        return {
            "max_bias": self.max_bias,
            "input_mask": self.in_mask,
            "output_mask": self.out_mask,
            "lat": self.lat.tolist()
        }

    def visualize(self, return_fig=False):
        fig, ax = plt.subplots(figsize=(6, 5))
        cax = ax.imshow(np.abs(self.lat), cmap='OrRd')
        ax.set_title("Linear Approximation Table (LAT)")
        ax.set_xlabel("Output Mask")
        ax.set_ylabel("Input Mask")
        fig.colorbar(cax)

        if return_fig:
            return fig
        else:
            plt.show()

class LinearAttack(Attack):
    def run(self, cipher, **kwargs) -> AttackResult:
        try:
            sbox = cipher.get_sbox()
        except AttributeError:
            raise ValueError("Cipher does not implement get_sbox(). Required for linear attack.")

        lat = compute_lat(sbox)
        bias_matrix = np.abs(lat / 16)
        input_mask, output_mask = np.unravel_index(np.argmax(bias_matrix[1:]), lat.shape)
        max_bias = bias_matrix[input_mask][output_mask]

        return LinearAttackResult(lat, max_bias, input_mask, output_mask)
