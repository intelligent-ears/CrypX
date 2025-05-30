from typing import Type
from core.interfaces import Cipher, Attack, AttackResult


class CrypXEngine:
    def __init__(self, cipher: Cipher):
        self.cipher = cipher
        self.attack_history = []

    def run_attack(self, attack: Type[Attack], **kwargs) -> AttackResult:
        print(f"[+] Running {attack.__name__} on {self.cipher.__class__.__name__}")
        attacker = attack(self.cipher)  
        result = attacker.run(**kwargs)
        self.attack_history.append((attack.__name__, result))
        return result

    def list_attacks_run(self):
        return [(name, result.summary()) for name, result in self.attack_history]

    def reset_history(self):
        self.attack_history.clear()
