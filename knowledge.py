
from pathlib import Path

# Find the project directory containing this Python file
PROJECT_DIR = Path(__file__).resolve().parent

# Location of our customer-support FAQ
FAQ_FILE = PROJECT_DIR / "knowledge_base" / "support_faq.txt"


def load_knowledge():
    """Load the customer-support FAQ from a text file."""
    if not FAQ_FILE.exists():
        raise FileNotFoundError(f"FAQ file not found: {FAQ_FILE}")

    with FAQ_FILE.open("r", encoding="utf-8") as file:
        content = file.read()

    return content


if __name__ == "__main__":
    knowledge = load_knowledge()
    print("Knowledge base loaded successfully!")
    print("-" * 40)
    print(knowledge)
