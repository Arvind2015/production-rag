from collections import Counter
import re
import math

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


def term_frequency(text):
    tokens = tokenize(text)
    return Counter(tokens)


document = "Redis is fast. Redis is commonly used for caching."

print(term_frequency(document))

def inverse_document_frequency(term, documents):
    document_count = len(documents)

    documents_containing_term = sum(
        1
        for document in documents
        if term in set(tokenize(document))
    )

    return math.log(
        document_count / (1 + documents_containing_term)
    )

print("IDF redis:", inverse_document_frequency("redis", documents))
print("IDF is:", inverse_document_frequency("is", documents))
print("IDF caching:", inverse_document_frequency("caching", documents))

def tf_idf(term, document, documents):
    tf = term_frequency(document)[term]
    idf = inverse_document_frequency(term, documents)

    return tf * idf

def score_document(query, document, documents):
    query_terms = set(tokenize(query))

    score = 0.0

    for term in query_terms:
        score += tf_idf(term, document, documents)

    return score

print("\nTF-IDF document scores:")

for document in documents:
    score = score_document(query, document, documents)
    print(f"{score:.3f} - {document}")    