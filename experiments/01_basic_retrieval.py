import re

documents = [
    "Redis is an in-memory data store commonly used for caching.",
    "Kafka is a distributed event streaming platform.",
    "PostgreSQL is a relational database system.",
    "Redis keeps frequently accessed data in memory so applications can retrieve it quickly."

]

query = "Which technology can be used for caching?"

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

def retrieve(query, documents):
    query_words = set(tokenize(query))

    results = []

    for document in documents:
        document_words = set(tokenize(document))

        score = len(query_words & document_words)

        results.append((score, document))

    return sorted(results, key=lambda x: x[0], reverse=True)


results = retrieve(query, documents)

for score, document in results:
    print(score, document)