
import re
from functools import lru_cache

from sentence_transformers import SentenceTransformer, util
from knowledge import load_knowledge


@lru_cache(maxsize=1)
def get_model():
    """Load the embedding model once and reuse it."""
    return SentenceTransformer("all-MiniLM-L6-v2")


def split_into_sections(text):
    """Split the FAQ into separate policy sections."""
    sections = re.split(r"\n\s*\n", text.strip())

    return [
        section.strip()
        for section in sections
        if section.strip()
    ]


@lru_cache(maxsize=1)
def get_knowledge_data():
    """Load policies and calculate their embeddings once."""
    sections = split_into_sections(load_knowledge())
    model = get_model()

    embeddings = model.encode(
        sections,
        convert_to_tensor=True
    )

    return sections, embeddings


def search_semantically(question, top_k=3):
    """Return policies ranked by semantic similarity."""
    model = get_model()
    sections, section_embeddings = get_knowledge_data()

    question_embedding = model.encode(
        question,
        convert_to_tensor=True
    )

    scores = util.cos_sim(
        question_embedding,
        section_embeddings
    )[0]

    count = min(top_k, len(sections))
    best_matches = scores.topk(count)

    results = []

    for index, score in zip(
        best_matches.indices.tolist(),
        best_matches.values.tolist()
    ):
        results.append({
            "section": sections[index],
            "similarity": round(float(score), 3)
        })

    return results


if __name__ == "__main__":
    question = input("Ask a customer-support question: ")

    for match in search_semantically(question):
        print(f"\nSimilarity: {match['similarity']}")
        print(match["section"])
