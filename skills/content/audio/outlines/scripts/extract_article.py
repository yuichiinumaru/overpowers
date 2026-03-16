import json
import outlines
from pydantic import BaseModel, Field

# Defines a reusable schema generator with outlines

class Article(BaseModel):
    title: str = Field(description="Title of the article")
    author: str = Field(description="Author name")
    word_count: int = Field(description="Number of words", gt=0)
    tags: list[str] = Field(description="List of tags")

def extract_article(text: str) -> Article:
    model = outlines.models.transformers("microsoft/Phi-3-mini-4k-instruct")
    generator = outlines.generate.json(model, Article)
    result = generator(f"Extract article details from: {text}")
    return result

if __name__ == "__main__":
    sample_text = "The Future of AI by John Doe is a 500-word piece on emerging trends in technology and machine learning."
    article = extract_article(sample_text)
    print(json.dumps(article.model_dump(), indent=2))
