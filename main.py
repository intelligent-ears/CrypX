import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def main():
    print("""
🔐 CrypX – Modular Cryptanalysis Framework
------------------------------------------
Analyze block ciphers using:
  • Differential Cryptanalysis
  • Linear Cryptanalysis
  • Algebraic Techniques

📦 Modules:
  - Built-in Ciphers: Mini-AES, PRESENT
  - Attacks: differential, linear, algebraic
  - Reports: PDF/Markdown, DDT/LAT visualizer

📂 Entry Points:
  - CLI Usage:    python cli.py --help
  - Streamlit UI: python streamlit_app.py (optional)

🛠️ Docs: See README.md or use --help in CLI
""")

    try:
        import cli
        cli.main()
    except Exception as e:
        print(f"❌ Failed to start CLI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

