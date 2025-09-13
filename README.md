# Generative AI Architectural Patterns

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Built with MkDocs](https://img.shields.io/badge/Built%20with-MkDocs-blue)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for-MkDocs-526CFE)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-green)](https://pages.github.com/)

🌐 **Live Site**: [https://dmccreary.github.io/genai-arch-patterns/](https://dmccreary.github.io/genai-arch-patterns/)

## Overview

This repository contains Dan McCreary and Steve Peterson's comprehensive guide to Generative AI Architectural Patterns. It serves as both an educational resource and practical reference for understanding and implementing generative AI systems in enterprise environments.

The documentation covers fundamental concepts, proven architectural patterns, and real-world implementation strategies for building scalable and effective generative AI applications.

## 📚 What's Inside

### Part 1: Core Concepts
- **Large Language Models (LLMs)** - Understanding the foundation of generative AI
- **Chatbots and Conversational AI** - Building interactive AI systems
- **Embeddings and Similarity** - Vector representations and semantic search
- **Knowledge Graphs** - Structured knowledge representation
- **Vector Databases** - Storage and retrieval systems for embeddings

### Part 2: Architectural Patterns
- **Prompt Enrichment** - Enhancing prompts for better results
- **Retrieval Augmented Generation (RAG)** - Combining retrieval with generation
- **Fine-tuning** - Customizing models for specific domains
- **AI Agents** - Autonomous AI systems with reasoning capabilities
- **Code Interpreters** - AI systems that can write and execute code
- **Knowledge Representation** - Storing and utilizing structured knowledge

## 🚀 Quick Start For Generating Your Own Custom Interactive Intelligent Textbook

### Prerequisites
- Python 3.7+
- pip
- Conda (recommended) or a Python VENV

### Local Development Setup

1. **Clone the repository**

```bash
git clone https://github.com/dmccreary/genai-arch-patterns.git
cd genai-arch-patterns
```

2. **Set up the environment**

```bash
# Using conda (recommended)
conda create -n mkdocs python=3
conda activate mkdocs

# Install dependencies
pip install mkdocs mkdocs-material
```

3. **Serve the site locally**

```bash
mkdocs serve
```

   The site will be available at `http://127.0.0.1:8000` with live reload enabled.

4. **Build for production**

```bash
mkdocs build
```

   The static site will be generated in the `/site` directory.

## 📁 Repository Structure

```
genai-arch-patterns/
├── docs/                    # Documentation content
│   ├── concepts/           # Foundational AI concepts
│   ├── patterns/           # Architectural patterns
│   ├── prompts/           # Example prompts and simulations
│   ├── img/               # Images and diagrams
│   └── index.md           # Main landing page
├── mkdocs.yml             # Site configuration
├── LICENSE                # CC BY-NC-SA 4.0 license
└── README.md             # This file
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/contributing.md) for details on how to:
- Report issues or suggest improvements
- Submit content additions or corrections
- Follow our style guidelines
- Respect the Creative Commons license terms

## 📄 License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please see our [Contact Page](docs/contact.md).

## 🙏 Acknowledgments

This project is built with and grateful for the following open source technologies:

### Core Technologies
- **[MkDocs](https://www.mkdocs.org/)** - A fast, simple and downright gorgeous static site generator that's geared towards building project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - A Material Design theme for MkDocs with beautiful styling and enhanced functionality

### MkDocs Extensions
- **[Python-Markdown](https://python-markdown.github.io/)** - A Python implementation of Markdown with extensive extension support
- **[PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - A collection of extensions for Python Markdown including:
  - **Highlight** - Syntax highlighting for code blocks
  - **SuperFences** - Enhanced fenced code blocks
  - **Details** - Collapsible content blocks
- **[Markdown Admonition](https://python-markdown.github.io/extensions/admonition/)** - Support for admonition blocks (notes, warnings, tips)
- **[Markdown Footnotes](https://python-markdown.github.io/extensions/footnotes/)** - Footnote support
- **[Markdown Attribute Lists](https://python-markdown.github.io/extensions/attr_list/)** - Add HTML attributes to Markdown elements
- **[Markdown Table of Contents](https://python-markdown.github.io/extensions/toc/)** - Automatic table of contents generation

### Infrastructure
- **[GitHub Pages](https://pages.github.com/)** - Free hosting for the documentation site
- **[Google Analytics](https://analytics.google.com/)** - Website analytics and insights

### Development Tools
- **[Python](https://www.python.org/)** - The programming language powering the build system
- **[Conda](https://conda.io/)** - Package management and virtual environment system

Special thanks to all the contributors and maintainers of these excellent open source projects that make this documentation possible.