# streamlit_app.py

import streamlit as st
import tempfile
import os
import sys
import traceback
import matplotlib.pyplot as plt

# Add root directory to sys.path to enable relative imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.dynamic_loader import load_cipher_class
from attacks.differential import DifferentialAttack
from attacks.linear import LinearAttack
from attacks.algebraic import AlgebraicAttack

st.set_page_config(page_title="CrypX – Web Cryptanalysis", layout="wide")
st.title("🔐 CrypX Web – Analyze Your Block Cipher")

st.markdown("""
Upload your custom block cipher Python file and choose the cryptanalysis method.
CrypX will analyze it and generate visual + textual reports.
""")

# File upload
uploaded_file = st.file_uploader("📂 Upload your cipher implementation (.py)", type="py")

# Attack selection
attack_name = st.selectbox("⚔️ Choose Attack", ["Differential", "Linear", "Algebraic"])

# Visualization toggle
visualize = st.checkbox("📊 Show Visualizations (DDT, LAT, etc)", value=True)

# Run button
run_btn = st.button("🚀 Run Analysis")

if run_btn and uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        # Load cipher class dynamically
        cipher = load_cipher_class(tmp_path)
        st.success("✅ Cipher class loaded successfully!")

        # Instantiate attack
        if attack_name == "Differential":
            attack = DifferentialAttack()
        elif attack_name == "Linear":
            attack = LinearAttack()
        elif attack_name == "Algebraic":
            attack = AlgebraicAttack()
        else:
            raise ValueError("Unknown attack selected")

        # Run the attack
        result = attack.run(cipher, visual=visualize)

        # Show summary
        st.markdown("### 📝 Summary Report")
        st.json(result.to_dict())

        # Show visualization
        if visualize:
            st.markdown("### 📊 Visualization")
            try:
                fig = result.visualize(return_fig=True)
                if fig:
                    st.pyplot(fig)
            except Exception as viz_err:
                st.warning(f"⚠️ Visualization error: {viz_err}")

        # Export section
        with st.expander("📄 Export Options"):
            st.download_button("Export as JSON", str(result.to_dict()), file_name="CrypX_Report.json")

    except Exception as e:
        st.error(f"❌ Failed to analyze: {e}")
        st.code(traceback.format_exc(), language="python")

    finally:
        os.remove(tmp_path)
