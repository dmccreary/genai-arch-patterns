# Retrieval-Augmented Generation (RAG)

# RAG (Retrieval-Augmented Generation) Pattern

A foundational pattern that enhances Large Language Models by retrieving relevant information from external knowledge bases before generating responses. This pattern combines the generative capabilities of LLMs with the accuracy and freshness of retrieved documents, reducing hallucinations and providing source attribution.

## When to Use

Use this pattern when you need to provide accurate, up-to-date information that may not be in the LLM's training data, when you require source attribution for generated content, or when working with proprietary or domain-specific knowledge bases. Ideal for customer support systems, knowledge management platforms, and technical documentation assistance.

## Architecture Drawing

The architecture shows a user query flowing through an embedding service to a vector store for similarity search, retrieving relevant documents that are combined with the original query and sent to an LLM for final response generation.

**Components:**
- User Interface (50, 50)
- Query Processing Service (200, 50)
- Embedding Service (350, 50)
- Vector Store (500, 50)
- Document Retrieval Service (650, 50)
- LLM Service (500, 200)
- Response Handler (200, 200)

**Edges:**
- User Interface → Query Processing Service: "User Query"
- Query Processing Service → Embedding Service: "Processed Query"
- Embedding Service → Vector Store: "Query Embedding"
- Vector Store → Document Retrieval Service: "Similar Documents"
- Document Retrieval Service → LLM Service: "Retrieved Context"
- Query Processing Service → LLM Service: "Original Query"
- LLM Service → Response Handler: "Generated Response"
- Response Handler → User Interface: "Final Answer"

## Related Patterns

Fine-tuned Model Pattern, Agentic RAG Pattern, Multi-Modal RAG Pattern

## References

1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) - 2020 - arXiv - Original paper introducing RAG methodology and its effectiveness in knowledge-intensive tasks
2. [RAG vs Fine-tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture](https://arxiv.org/abs/2401.08406) - 2024 - arXiv - Comprehensive comparison of RAG versus fine-tuning approaches for domain-specific applications
3. [Seven Failure Points When Engineering a Retrieval Augmented Generation System](https://arxiv.org/abs/2401.05856) - 2024 - arXiv - Practical guide identifying common pitfalls and solutions in RAG implementation

## Description
A variation of [Prompt Enrichment](./prompt-enrichment.md) where a search engine is used to add additional knowledge to a prompt to increase
response output.

RAG is often used as a lower-cost method for including local knowledge
with general knowledge.

Many RAG designs focus on the use of a [Vector Database](../concepts/vector-database.md) to find text that is similar to a given prompt.

RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia.

## References

1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks1](https://arxiv.org/abs/2005.11401) Patrick Lewis et. el - 12 Apr 2021

2. [KD Nuggets](https://www.kdnuggets.com/rag-vs-finetuning-which-is-the-best-tool-to-boost-your-llm-application)