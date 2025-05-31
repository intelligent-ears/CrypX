import os
from datetime import datetime
from fpdf import FPDF
import matplotlib.pyplot as plt
import tempfile

class ReportGenerator:
    def __init__(self, output_dir="reports/output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def export_markdown(self, attack_result, cipher_name, attack_name):
        filename = f"{cipher_name}_{attack_name}_report.md"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w") as f:
            f.write(f"# 🔐 CrypX Attack Report\n")
            f.write(f"**Cipher**: {cipher_name}\n\n")
            f.write(f"**Attack**: {attack_name}\n")
            f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## 📊 Summary\n")
            f.write(f"{attack_result.summary()}\n\n")

            f.write(f"## 🔢 Raw Data\n")
            f.write(f"```json\n{attack_result.to_dict()}\n```\n")

        return filepath

    def export_pdf(self, attack_result, cipher_name, attack_name):
        filename = f"{cipher_name}_{attack_name}_report.pdf"
        filepath = os.path.join(self.output_dir, filename)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="🔐 CrypX Attack Report", ln=True, align='C')
        pdf.ln(5)
        pdf.cell(200, 10, txt=f"Cipher: {cipher_name}", ln=True)
        pdf.cell(200, 10, txt=f"Attack: {attack_name}", ln=True)
        pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
        pdf.ln(5)
        pdf.multi_cell(0, 10, txt="Summary:\n" + attack_result.summary())

        if hasattr(attack_result, "visualize"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_img:
                attack_result.visualize()
                plt.savefig(tmp_img.name)
                pdf.image(tmp_img.name, w=150)
                os.unlink(tmp_img.name)

        pdf.output(filepath)
        return filepath

