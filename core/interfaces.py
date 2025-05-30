# core/interfaces.py

from abc import ABC, abstractmethod

class Cipher(ABC):
    """
    Abstract base class for all block ciphers.
    """

    @abstractmethod
    def encrypt(self, plaintext: bytes, key: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        pass

    @abstractmethod
    def get_sbox(self) -> list:
        """Returns the S-box as a list or matrix for analysis."""
        pass

    @abstractmethod
    def block_size(self) -> int:
        """Returns block size in bits."""
        pass

    @abstractmethod
    def key_size(self) -> int:
        """Returns key size in bits."""
        pass


class Attack(ABC):
    """
    Abstract base class for all attack strategies.
    """

    @abstractmethod
    def run(self, cipher: Cipher, **kwargs) -> 'AttackResult':
        pass


class AttackResult(ABC):
    """
    Abstract base class for results of cryptanalysis.
    """

    @abstractmethod
    def summary(self) -> str:
        """Returns a human-readable summary of the result."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Returns the result as a dictionary for reporting."""
        pass

    @abstractmethod
    def visualize(self):
        """Optional: Generate visualization using matplotlib or similar."""
        pass

