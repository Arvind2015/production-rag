import math
from sentence_transformers import SentenceTransformer


texts = [
    "Redis is used for caching.",
    "Redis keeps frequently accessed information readily available.",
    "Kafka processes distributed events.",
    "PostgreSQL stores relational data."
]


model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

embeddings = model.encode(texts)

for text, embedding in zip(texts, embeddings):
    print(text)
    print("Vector dimensions:", len(embedding))
    print("First 10 values:", embedding[:10])
    print()


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


#query = "Redis keeps frequently accessed information readily available."
query = "Keep things snappy by throwing hot keys into Redis."

query_vector = model.encode([query])[0]

print("Query vector:")
print("Vector dimensions:", len(query_vector))
print("First 10 values:", query_vector[:10])
print()

print("Similarities:")

for text, vector in zip(texts, embeddings):

    similarity = cosine_similarity(
        query_vector,
        vector
    )

    print(f"{similarity:.3f} - {text}")