# PubMed CLI Tool

## 🧠 Project Overview
This is a command-line tool built for Aganitha Cognitive Solutions' Backend Internship Hackathon. It enables you to search for recent PubMed research articles, extract metadata, filter out academic publications, and save the results to a CSV file.

The project was developed in **Python** using **Poetry** as a package manager and environment handler.

---

## ⚙️ Features
- Query PubMed using search keywords.
- Fetch metadata for the top 20 articles.
- Detect if an article has at least one **non-academic author** based on affiliation.
- Save filtered results in a structured CSV file.
- Debug mode available to print full metadata for inspection.

---

## 📁 Folder Structure
```
aganitha_backend_project/
│
├── fetch_metadata.py        # Main CLI script
├── results.csv              # Sample output file (optional)
├── pyproject.toml           # Poetry project config
├── poetry.lock              # Poetry lock file
└── README.md                # This file
```

---

## 🛠️ Setup Instructions
### 1. Clone or Copy the Project Folder
Place the folder where you have Python 3.13 and Poetry installed.

### 2. Install Dependencies
```bash
poetry install
```

This will automatically create a virtual environment and install `biopython` and `numpy`.

---

## 🚀 How to Run
Use the following command to run the CLI and fetch metadata:

```bash
poetry run python fetch_metadata.py --query "brain tumor" --file results.csv
```

### ✅ Arguments:
- `--query`  : PubMed search term (required)
- `--file`   : Output file name to save filtered results (optional)
- `--debug`  : Enable debug logs to print all paper metadata (optional)

Example with debug:
```bash
poetry run python fetch_metadata.py --query "machine learning cancer" --file cancer_results.csv --debug
```

---

## 🧪 Example Output
Each result will include:
- PMID
- Title
- Date
- Authors
- Affiliations
- Emails (if available)

---

## 🧑‍💻 Author
- **Sameer Kumar G V**  
  Email: sameerkumarg508@gmail.com

---

## 📌 Notes
- Only articles with at least one **non-academic affiliation** are saved.
- Academic keywords filtered: `university`, `institute`, `college`, `school`, `hospital`, `department`, `centre`

---

## 📦 Dependencies
- Python >= 3.13
- Biopython
- NumPy

These are managed via Poetry (`pyproject.toml`).

---

## ✅ Submission Ready
You can now zip the project folder or push it to GitHub as your final submission.

---
