# RAG Learning Context

## Project

Hands-on RAG learning repository accompanying:

**Production RAG and GenAI Systems**

The goal is to understand RAG systems from first principles by implementing
key concepts ourselves before using production libraries and services.

---

## Learning Approach

The learning sequence is:

1. Understand the concept
2. Implement a small version in Python
3. Run it and inspect the actual numbers/output
4. Discuss why the result occurs
5. Only then capture the polished explanation in the book

Do not jump directly to production libraries or abstractions before the
underlying concept is understood.

---

## Current Progress

### Completed: Lexical Retrieval

File:

`experiments/01_basic_retrieval.py`

Implemented from scratch:

- Tokenization
- Keyword retrieval
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- TF-IDF
- Shared vocabulary
- Document vectors
- Sparse-vector concept
- Query vectors
- Dot product
- Vector magnitude
- Cosine similarity
- Document ranking

### Current example

Documents:

1. Redis is an in-memory data store commonly used for caching.
2. Kafka is a distributed event streaming platform.
3. PostgreSQL is a relational database system.
4. Redis keeps frequently accessed data in memory so applications can
   retrieve it quickly.

Query:

`Which technology can be used for caching?`

Latest verified cosine-similarity ranking:

```text
0.580 - Redis is an in-memory data store commonly used for caching.
0.161 - Redis keeps frequently accessed data in memory so applications can retrieve it quickly.
0.000 - Kafka is a distributed event streaming platform.
0.000 - PostgreSQL is a relational database system.