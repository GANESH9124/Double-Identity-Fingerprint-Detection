# 🔍 Double Identity Fingerprint Detection

A Python-based project for detecting **double identity fingerprints**, where a fingerprint image may represent a spoof or a morphed version of two identities.

This can help in detecting fake biometrics in systems relying on fingerprint authentication — useful in security applications, biometric verification systems, and forensic analysis.

---

## 📂 Project Structure
```text
Double-Identity-Fingerprint-Detection/
├── double_identity_fingerprint.py   # Main script for fingerprint analysis
├── fingerprint_sample.jpg           # Sample fingerprint image used for testing
└── README.md                        # Project documentation
```


---

## 🧠 How It Works

The detection algorithm includes:

- **Image preprocessing** (grayscale, blur, edge detection)
- **Feature analysis** (contours, shape metrics)
- **Decision logic** for detecting spoofed or manipulated fingerprint patterns

---

## ▶️ Run the Code

### ✅ Prerequisites

Make sure you have Python 3 and the following libraries installed:

```bash
pip install opencv-python numpy
```
```bash
python double_identity_fingerprint.py
```

## 📃 License


This project is under the MIT License.
