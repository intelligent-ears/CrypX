from abc import ABC, abstractmethod

class Cipher(ABC):
    @abstractmethod
    def encrypt(self, plaintext: bytes, key: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: bytes, key: bytes) -> bytes:
        pass

    @abstractmethod
    def get_sbox(self) -> list:
        pass

    @abstractmethod
    def block_size(self) -> int:
        pass

    @abstractmethod
    def key_size(self) -> int:
        pass


class Attack(ABC):
    @abstractmethod
    def run(self, cipher: Cipher, **kwargs) -> 'AttackResult':
        pass


class AttackResult(ABC):
    @abstractmethod
    def summary(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def visualize(self):
        pass

