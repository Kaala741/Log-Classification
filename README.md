# Log Classification System using Llama, BERT, NLP & Regex
## 🚀 **Project Overview**

This project is an AI-powered log analysis system that automatically parses, classifies, and explains large-scale application logs in real time. 
It integrates Regex-based extraction, BERT-based semantic classification, and Llama-powered reasoning to detect anomalies, categorize logs, and summarize root causes for system incidents.

---

## 🧩  **Features**

- **Regex-based Log Parsing** : Extracts structured data like timestamps, error codes, IPs, and stack traces from unstructured logs.

- **BERT Classification** : Categorizes logs into classes such as INFO, WARN, ERROR, SECURITY_ALERT, and PERFORMANCE_ISSUE.

- **Llama Reasoning** : Provides context-aware explanations and human-readable summaries for complex or multi-line log events.

- **NLP Preprocessing** : Tokenization, vector embeddings, and keyword normalization for improved semantic understanding.

- **Real-Time Pipeline** : Built with Python, FastAPI, and Kafka to handle streaming logs efficiently.

- **Human-in-the-Loop Learning** : Supports feedback to continuously improve classification accuracy.

---

## 📈 **Impact**

1.Reduced log triage and root-cause detection time by ~70%.

2.Enabled proactive anomaly detection and faster incident response.

3.Demonstrated a hybrid AI system combining rule-based, transformer, and generative AI reasoning.

---

## 🛠 **Tech Stack**

- **Language & Frameworks** : Python, FastAPI

- **AI Models** : BERT (Hugging Face Transformers), Llama 3

- **Tools & Libraries** : Regex, NLP preprocessing tools

---

## **File Structure** :
``` 
Log-Classification/
├── main.py                      # FastAPi app script
├── classify.py                  # Orchestrator script for classification
├── processor_bert.py            # BERT-based classification
├── processor_llm.py             # LLM (Llama) reasoning
├── processor_regex.py           # Regex-based log parsing
├── models/                     # Saved model weights, config files
│   └── log_classifier.joblib
├── requirements.txt             # List of dependencies
├── resources/                  # External resources / sample logs / labels
│   └── output.csv
|   └── test.csv
├── README.md                    # readme file
└── training/                    # Training scripts or notebooks
    ├── Dataset/
    |   └── test.csv
    └── log_classification.ipynb
```

---

## 📦 **Installation & Usage**

**Clone the repository**:

```
git clone https://github.com/Kaala741/Log-Classification.git
cd Log-Classification
```

**Create a virtual environment**:

```
python -m venv .venv
.venv\Scripts\activate
```

**Install dependencies**:

```
pip install -r requirements.txt
```

**Run the API server**:
```
uvicorn main:app --reload
```

Use the endpoints to stream logs, classify them, and get summaries.

Note: Do not commit .env or other sensitive files. Add them to .gitignore.

----
## 🔒 **Security & Best Practices**

Secrets (API keys, passwords) must never be committed.

.env, .venv, .idea, and other sensitive files are included in .gitignore.
 
---
## **License** 
This project is licensed under the MIT License. See the LICENSE file for details.

---
