# What Problem Does RAG Solve?

Retrieval-Augmented Generation (RAG) combines information retrieval with
language-model generation.

The basic idea is simple: instead of asking a language model to answer a
question using only the knowledge encoded in its parameters, a RAG system
first retrieves relevant information from an external knowledge source and
provides that information to the model as context.

The process can be represented as:

User Question
     |
     v
Retrieve Relevant Information
     |
     v
Construct Context
     |
     v
Language Model
     |
     v
Generated Answer

The retrieval step is important because real-world applications often need
to answer questions using information that is specific to an organisation,
application, or continuously changing knowledge base.

A small collection of documents could theoretically be included directly in
a prompt. That approach becomes impractical as the knowledge base grows,
however. A production system may contain thousands or millions of documents.

RAG therefore introduces an information-selection stage:

Large Knowledge Base
        |
        v
Relevant Information
        |
        v
Language Model Context
        |
        v
Answer

This makes RAG fundamentally an information retrieval problem as well as a
generation problem.

## A Simple Starting Point

Before introducing embeddings or vector databases, it is useful to consider
the simplest possible retrieval mechanism: keyword matching.

Given a collection of documents, a basic retriever can look for words from
the user's question inside each document and rank documents according to the
number of matching words.

Although this approach is extremely limited, it provides an important
baseline. It also exposes a fundamental problem: words that are different
lexically may still have similar meanings.

For example, a user might ask about "caching" while a document describes
"keeping frequently accessed data in memory."

A keyword-based system may fail to recognise that these statements are
related.

This limitation leads naturally to the idea of semantic representations,
which is where embeddings become useful.