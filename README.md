# CodeOrbit AI Support Assistant

An AI-powered customer support chatbot built with **Python, FastAPI, Sentence Transformers, HTML, CSS, and JavaScript**. It uses semantic search to find relevant answers from a customer support knowledge base, even when users phrase questions differently from the original policies.

## Features

- **AI-powered semantic search** using Sentence Transformers.
- **Customer support knowledge base** containing return, shipping, cancellation, payment, and support policies.
- **Interactive chat interface** for asking questions and viewing answers.
- **FastAPI REST API** for processing questions.
- **Swagger API documentation** for testing endpoints.
- **Responsive interface** designed to work on desktop and mobile screens.
- **Relevance threshold** to help avoid returning answers when a match is too weak.

## Screenshot
**Home Page**

![Home](https://github.com/mohamud007/AI-Support-Assistant/blob/main/Screenshot%202026-10-25%20190249.png)

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API |
| Sentence Transformers | Semantic text embeddings |
| PyTorch | Embedding model support |
| HTML | Chat interface structure |
| CSS | Interface styling |
| JavaScript | Chat interactions and API requests |
| Uvicorn | Local development server |

## Project Structure

```text
Ai-Support-Assisstance-project/
├── knowledge_base/
│   └── support_faq.txt
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── knowledge.py
├── main.py
├── search_knowledge.py
├── semantic_search.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or later (Python 3.13 was used during development).
- pip
- Git (optional, for cloning the repository)

### 1. Clone the repository

Replace `mohamudsk007` with your GitHub username after publishing the project.

```bash
git clone https://github.com/mohamudsk007/AI-Support-Assistant.git
cd AI-Support-Assistant
```

Alternatively, open your existing project folder in VS Code and continue with the next step.

### 2. Create a virtual environment

**Windows:**

```bash
py -3.13 -m venv .venv
```

Activate it in Command Prompt:

```bat
.venv\Scripts\activate.bat
```

For PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The first run of semantic search may download the embedding model, so an internet connection is needed initially.

### 4. Run the application

```bash
python -m uvicorn main:app --reload
```

### 5. Open the application

- **Chat interface:** http://127.0.0.1:8000/
- **API documentation:** http://127.0.0.1:8000/docs
- **Health endpoint:** http://127.0.0.1:8000/health

Keep the terminal running while using the application.

## Example Questions

Try asking:

- How do I get my money back?
- How many days does delivery take?
- Can I cancel an order that has already shipped?
- What payment methods are accepted?
- When is customer support available?

The assistant searches the knowledge base for the most relevant policy and displays the matching content.

## API Endpoint

### Ask a question

**Endpoint:** `POST /ask`

Example request:

```json
{
  "question": "How do I get my money back?"
}
```

The response includes the original question, the matching policy text, and a similarity score when a sufficiently relevant match is found.

## How It Works

1. The user enters a question in the chat interface.
2. JavaScript sends the question to the FastAPI `/ask` endpoint.
3. Sentence Transformers converts the question and knowledge-base sections into embeddings.
4. Cosine similarity ranks the sections by semantic relevance.
5. The application returns the best matching policy if its relevance score meets the configured threshold.
6. The chat interface displays the answer.

## Current Limitations

- Answers are based on the supplied knowledge base, not live company systems.
- Semantic similarity does not guarantee factual correctness.
- The project does not currently connect to an order-management system or customer database.
- The embedding model may need to download on the first run.

## Future Improvements

- Add conversation history and timestamps.
- Improve handling of unrelated or ambiguous questions.
- Add automated tests for API endpoints and search behavior.
- Deploy the application online.
- Add more support policies and expand the knowledge base.
