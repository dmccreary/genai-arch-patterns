# Retrieval-Augmented Generation (RAG)

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