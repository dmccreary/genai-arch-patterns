# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Dan McCreary's Generative AI Architectural Patterns project - a comprehensive documentation site covering concepts and patterns for generative AI systems. The site is built using MkDocs with the Material theme and is deployed to GitHub Pages.

## Development Commands

### Building and Serving the Site
```bash
# Install dependencies (first time setup)
conda create -n mkdocs python=3
conda activate mkdocs
pip install mkdocs mkdocs-material

# Build the static site
mkdocs build

# Serve locally for development (with live reload)
mkdocs serve
```

The built site will be generated in the `/site` directory. Local development server runs on `http://127.0.0.1:8000`.

## Architecture and Structure

### Content Organization
- **`docs/`** - All markdown content for the site
  - **`concepts/`** - Foundational generative AI concepts (LLMs, embeddings, agents, etc.)
  - **`patterns/`** - Architectural patterns (RAG, prompt enrichment, finetuning, etc.)
  - **`prompts/`** - Example prompts and knowledge graph simulations
  - **`img/`** - Images and diagrams
  - **`index.md`** - Main landing page

### Key Files
- **`mkdocs.yml`** - Site configuration, navigation structure, theme settings, and analytics
- **`README.md`** - Development setup instructions
- **`.vscode/`** - VS Code workspace configuration

### Content Structure
The site follows a two-part structure:
1. **Part 1: Concepts** - Foundational knowledge (LLMs, chatbots, embeddings, knowledge graphs)
2. **Part 2: Patterns** - Implementation patterns (prompt enrichment, agents, RAG, code interpreters)

### Navigation
Navigation is defined in `mkdocs.yml` and includes automatic page discovery. The site uses Material theme features like navigation expansion, breadcrumbs, and prev/next footer navigation.

## Content Guidelines

- All content is in Markdown format
- Licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
- Uses MkDocs extensions for code highlighting, admonitions, footnotes, and table of contents
- Images should be placed in `docs/img/` directory
- Internal links should use relative paths

## Deployment

The site is automatically deployed to GitHub Pages. The live site is available at: https://dmccreary.github.io/genai-arch-patterns/