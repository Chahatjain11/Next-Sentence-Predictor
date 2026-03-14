# 🧠 Next Sentence Predictor

A simple and interactive web app that uses **GPT-2** (via Hugging Face Transformers) to predict the next possible sentences from any user-provided input.

---

## 🚀 Features

- Type any sentence and get AI-generated continuations
- Choose how many predictions you want (1–5)
- Built with Streamlit for a clean, interactive UI
- Runs fully locally — no API key needed

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Chahatjain11/Next-Sentence-Predictor.git
cd Next-Sentence-Predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python3 -m streamlit run app.py
```

**4. Open your browser at** `http://localhost:8501`

> Note: First run will download the GPT-2 model (~500MB). This only happens once.

---

## 📸 How It Works

1. Enter any sentence in the text box
2. Select how many predictions you want using the slider
3. Click **Predict**
4. GPT-2 generates the most likely sentence continuations

---

## 👩‍💻 Author

**Chahat Jain** — [GitHub](https://github.com/Chahatjain11) · [LinkedIn](https://linkedin.com/in/chahat-jain-676052327)
