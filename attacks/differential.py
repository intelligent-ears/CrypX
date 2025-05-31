import numpy as np
from core.interfaces import Attack, AttackResult
from utils.sbox import compute_ddt
import matplotlib.pyplot as plt

class DifferentialAttackResult(AttackResult):
    def __init__(self, ddt, max_probability, input_diff, output_diff):
        self.ddt = ddt
        self.max_prob = max_probability
        self.in_diff = input_diff
        self.out_diff = output_diff

    def summary(self):
        return (f"Max differential probability: {self.max_prob:.4f} "
                f"for input_diff=0x{self.in_diff:X}, output_diff=0x{self.out_diff:X}")

    def to_dict(self):
        return {
            "max_probability": self.max_prob,
            "input_diff": self.in_diff,
            "output_diff": self.out_diff,
            "ddt": self.ddt.tolist()
        }

    def visualize(self, return_fig=False):
        fig, ax = plt.subplots(figsize=(6, 5))
        cax = ax.imshow(self.ddt, cmap='Blues')
        ax.set_title("Difference Distribution Table (DDT)")
        ax.set_xlabel("Output Difference")
        ax.set_ylabel("Input Difference")
        fig.colorbar(cax)

        if return_fig:
            return fig
        else:
            plt.show()



class DifferentialAttack(Attack):
    def run(self, cipher, **kwargs) -> AttackResult:
        try:
            sbox = cipher.get_sbox()
        except AttributeError:
            raise ValueError("Cipher does not implement get_sbox(). Required for differential attack.")

        ddt = compute_ddt(sbox)
        max_prob = np.max(ddt[1:] / 16)  
        in_diff, out_diff = np.unravel_index(np.argmax(ddt), ddt.shape)

        return DifferentialAttackResult(ddt, max_prob, in_diff, out_diff)
