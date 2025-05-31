from sympy import symbols, Eq
import matplotlib.pyplot as plt
from core.interfaces import Attack, AttackResult


class AlgebraicAttackResult(AttackResult):
    def __init__(self, equations, solution):
        self.equations = equations
        self.solution = solution

    def summary(self):
        if self.solution:
            return f"Algebraic solution found: {self.solution}"
        return "No solution found."

    def to_dict(self):
        return {
            "equations": [str(eq) for eq in self.equations],
            "solution": self.solution
        }

    def visualize(self, return_fig=False):
        fig, ax = plt.subplots()

        eq_text = "\n".join([str(eq) for eq in self.equations])
        ax.axis("off")
        ax.set_title("Algebraic Equations")
        ax.text(0, 0.5, eq_text, fontsize=12, va="center", ha="left", wrap=True)

        if return_fig:
            return fig
        else:
            plt.show()


class AlgebraicAttack(Attack):
    def __init__(self, cipher=None):
        self.cipher = cipher

    def run(self, cipher=None, **kwargs) -> AttackResult:
        target_cipher = cipher or self.cipher

        k = symbols('k')
        pt = kwargs.get("plaintext", 1)
        ct = kwargs.get("ciphertext", 3)

        eq = Eq((pt + k) % 16, ct)
        equations = [eq]

        # Try all possible values of k (0–15)
        valid_k = [guess for guess in range(16) if (pt + guess) % 16 == ct]

        return AlgebraicAttackResult(equations, valid_k if valid_k else None)
