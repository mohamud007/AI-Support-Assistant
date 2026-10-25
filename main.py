
from fastapi import FastAPI
from pydantic import BaseModel
from knowledge import load_knowledge
from semantic_search import search_semantically
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(title="CodeOrbit AI Support Assistant")
BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "CodeOrbit AI Support Assistant"
    }


@app.get("/knowledge")
def get_knowledge():
    return {
        "knowledge_base": load_knowledge()
    }



@app.post("/ask")
def ask_question(request: QuestionRequest):
    question = request.question.strip()

    if not question:
        return {
            "question": question,
            "answer": "Please enter a question."
        }

    matches = search_semantically(question, top_k=1)

    if not matches:
        return {
            "question": question,
            "answer": "Sorry, no relevant information was found."
        }

    best_match = matches[0]

    # Avoid returning a policy when the match is too weak.
    if best_match["similarity"] < 0.25:
        return {
            "question": question,
            "answer": "Sorry, I couldn't find a sufficiently relevant policy."
        }

    return {
        "question": question,
        "answer": best_match["section"],
        "similarity": best_match["similarity"]
    }
