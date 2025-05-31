import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import argparse
from core.engine import CrypXEngine
from ciphers.mini_aes import MiniAES
from ciphers.present import PRESENT
from attacks.differential import DifferentialAttack
from attacks.linear import LinearAttack
from attacks.algebraic import AlgebraicAttack
from reports.generator import ReportGenerator
from reports.visualizer import plot_ddt, plot_lat

CIPHER_MAP = {
    "mini-aes": MiniAES,
    "present": PRESENT,
}

ATTACK_MAP = {
    "differential": DifferentialAttack,
    "linear": LinearAttack,
    "algebraic": AlgebraicAttack,
}

def list_options():
    print("\nSupported Ciphers:")
    for name in CIPHER_MAP:
        print(f"  - {name}")
    print("\nSupported Attacks:")
    for name in ATTACK_MAP:
        print(f"  - {name}")
    print()

def main():
    parser = argparse.ArgumentParser(description="🔐 CrypX: Modular Cryptanalysis Framework")
    parser.add_argument("--cipher", type=str, required=True, help="Cipher to analyze (e.g., mini-aes, present)")
    parser.add_argument("--attack", type=str, required=True, help="Attack type (e.g., differential, linear, algebraic)")
    parser.add_argument("--export", choices=["md", "pdf"], help="Export report format")
    parser.add_argument("--visual", action="store_true", help="Show visualization (DDT/LAT/etc.)")
    parser.add_argument("--list", action="store_true", help="List supported ciphers and attacks")

    args = parser.parse_args()

    if args.list:
        list_options()
        return

    cipher_cls = CIPHER_MAP.get(args.cipher.lower())
    attack_cls = ATTACK_MAP.get(args.attack.lower())

    if not cipher_cls or not attack_cls:
        print("❌ Invalid cipher or attack. Use --list to see supported options.")
        return

    cipher = cipher_cls()
    attack = attack_cls(cipher)

    print(f"\n🔍 Running {args.attack} attack on {args.cipher.upper()}...\n")
    result = attack.run()
    print("✅ Attack Summary:\n")
    print(result.summary())

    if args.visual:
        if args.attack == "differential":
            plot_ddt(result.ddt)
        elif args.attack == "linear":
            plot_lat(result.lat)

    if args.export:
        reporter = ReportGenerator()
        if args.export == "md":
            path = reporter.export_markdown(result, args.cipher, args.attack)
        else:
            path = reporter.export_pdf(result, args.cipher, args.attack)
        print(f"\n📄 Report exported: {path}")

if __name__ == "__main__":
    main()

