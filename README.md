# 🔐 CrypX – Modular Cryptanalysis Framework

CrypX is a **web-based cryptanalysis framework** that allows users to **analyze custom block cipher implementations** using well-known techniques like:

- 🧮 **Differential Cryptanalysis**
- 📊 **Linear Cryptanalysis**
- 🧠 **Algebraic Attacks**

The goal is to support cryptographers, researchers, and students in studying and testing the strength of block ciphers through visualization and reporting.

---

## 🚀 Features

- ✅ Upload custom Python-based block cipher implementations
- 🧠 Apply multiple cryptanalytic techniques
- 📈 Visual reports like DDT (Difference Distribution Table) and LAT (Linear Approximation Table)
- 📄 Download results in JSON format
- 🌐 Streamlit-based interactive web interface

---

## 🧱 Module Structure

```text
CrypX/
│
├── core/
│   ├── interfaces.py       
│   └── engine.py
|
├── attacks/
│   ├── differential.py      
│   ├── linear.py            
│   └── algebraic.py        
│
├── utils/
│   ├── sbox.py
|   ├── matrix.py
|   ├── gf.py          
│   └── dynamic_loader.py   
│
├── reports/
│   ├── generator.py
|   └── visualozer.py       
│
├── main.py
├── cli.py      
├── streamlit_app.py
├── requirements.txt    
└── README.md   
```
---

## 🧑‍💻 How It Works

1. **Upload Cipher**:
   - Users upload a `.py` file containing their block cipher class (must implement methods like `get_sbox()`).

2. **Choose Attack**:
   - Pick from Differential, Linear, or Algebraic attack from dropdown.

3. **Visualization**:
   - Toggle visual representation of attack artifacts (DDT heatmaps, etc).

4. **Result**:
   - View summary and detailed result
   - Download JSON report

---

## ⚙️ Running Locally

### 1. Clone the Repo

```bash
git clone https://github.com/intelligent-ears/CrypX.git
cd CrypX
```
---
## 🌐 Try Online

CrypX is also deployed via **Streamlit Cloud**:

👉 [**Open Web App**](https://crypx0.streamlit.app)

No installation needed — upload your cipher and analyze directly in the browser!

---

##🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest new cryptanalysis methods.

To contribute:

    1. Fork the repository
    
    2. Create a feature branch
    
    3. Submit a PR


© 2025 **intelligent-ears**
