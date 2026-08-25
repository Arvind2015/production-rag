import math



texts = [
    "Redis is used for caching.",
    "Redis stores frequently accessed data in memory.",
    "Kafka processes distributed events.",
    "PostgreSQL stores relational data."
]


def toy_embedding(text):
    text = text.lower()

    caching = 1.0 if "caching" in text or "cache" in text else 0.0
    memory = 1.0 if "memory" in text or "stores" in text else 0.0
    events = 1.0 if "kafka" in text or "events" in text else 0.0

    return [caching, memory, events]


for text in texts:
    vector = toy_embedding(text)

    print(text)
    print(vector)
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

query = "Redis keeps frequently accessed information readily available."

query_vector = toy_embedding(query)

print("Query:")
print(query_vector)
print()

print("Similarities:")

for text in texts:
    vector = toy_embedding(text)

    similarity = cosine_similarity(
        query_vector,
        vector
    )

    print(f"{similarity:.3f} - {text}")