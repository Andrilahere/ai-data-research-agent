
# AI Data & Research Intelligence Agent

An AI-powered platform to analyze research papers and datasets.

* Summarizes PDF research papers
* Extracts keywords, methods, and results
* Answers natural language questions from CSV, Excel, or PDF files
* Generates simple charts from datasets

Built with **FastAPI**, **Streamlit**, **LangChain**, and **OpenAI GPT-4/5**.

---

## Features

* **Research Assistant Agent**: Summarize papers, extract keywords/methods/results, or perform Q\&A.
* **Data Intelligence Agent**: Query CSV/Excel datasets using natural language and generate charts.
* **Hybrid Architecture**: Automatically routes PDF files to research agent, and tabular files to data agent.
* **Easy-to-use interface** via browser.

---

## Requirements

* Python 3.10+
* [OpenAI API Key](https://platform.openai.com/account/api-keys)
* Libraries in `requirements.txt`:

```text
fastapi
uvicorn
streamlit
python-dotenv
pandas
matplotlib
PyMuPDF
langchain
faiss-cpu
openai
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/ai-data-research-agent.git
cd ai-data-research-agent
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4. Set OpenAI API Key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=sk-your_openai_key_here
```

Your FastAPI backend automatically loads this key.

---

### 5. Run the backend server

```bash
uvicorn app.main:app --reload
```

* Backend runs at: `http://127.0.0.1:8000`

---

### 6. Run the Streamlit frontend

```bash
streamlit run streamlit_app.py
```

* Frontend opens in your browser
* Upload CSV/Excel/PDF files and type queries

---

### 7. Usage

* **Upload a file** (CSV, XLSX, PDF)
* **Type your question** in natural language
* **Get response** as JSON, summary, or chart

---

### 8. Notes

* CSV/Excel → Data Intelligence Agent
* PDF → Research Assistant Agent
* Charts are returned as base64-encoded images (for embedding in frontend)

---

### 9. Example Queries

* **Data agent:** "Show the top 5 rows", "Plot sales by month"
* **Research agent:** "Summarize this paper", "Extract keywords and methods"


### 10. Security

* Never share your OpenAI API key publicly
* Ensure uploaded files do not contain sensitive information


