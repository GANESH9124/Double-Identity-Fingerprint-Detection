# 🔍 Double Identity Fingerprint Detection

A Python-based project for detecting **double identity fingerprints**, where a fingerprint image may represent a spoof or a morphed version of two identities.

This can help in detecting fake biometrics in systems relying on fingerprint authentication — useful in security applications, biometric verification systems, and forensic analysis.

---
## 🌐 Live Demo

🚀 Try the web app here:  
👉 [https://dif.onrender.com/](https://dif.onrender.com/)

You can upload a fingerprint image and get an instant analysis in your browser.

---

## 📂 Project Structure
```text
Double-Identity-Fingerprint-Detection/
├── instance/                          # Directory for instance-specific files
├── models/                            # Directory for machine learning models
├── static/                            # Static files (e.g., CSS, JavaScript)
├── templates/                         # HTML templates for Flask app
├── uploads/                           # Directory for uploaded fingerprint images
├── DOUBLE IDENTITY FINGERPRINT DETECTION.pptx  # Project presentation
├── README.md                          # Project documentation
├── app.py                             # Flask web application script
├── dfp1.jpg                           # Sample fingerprint image 1
├── dfp2.jpg                           # Sample fingerprint image 2
├── mix_of_dfp.jpg                     # Sample image of mixed fingerprints
├── real.jpg                           # Sample real fingerprint image
├── real1.jpg                          # Another sample real fingerprint image
└── requirements.txt                   # List of dependencies

```


---

## 🧠 How It Works

- Uses image processing with OpenCV to extract features from fingerprint images
- Analyzes contour patterns to identify inconsistencies or double identity artifacts
- Provides results via CLI or a web interface (Flask)

---

## ▶️ Run the Code Locally 

### ✅ Prerequisites

Make sure you have Python 3 and the following libraries installed:

```bash
pip install opencv-python numpy flask
```
```bash
python double_identity_fingerprint.py
```
```bash
python app.py
```
## 📃 License


This project is under the MIT License.
