# Generative AI Architectural Patterns

Site: 
[https://dmccreary.github.io/genai-arch-patterns/](https://dmccreary.github.io/genai-arch-patterns/)

This GitHub repo supports Dan McCreary's Generative AI Patterns project.

The content is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

See the [LIECNSE](./LICENSE) file for details.

The site was created with [mkdocs](mkdocs.org) using the [Material Theme](https://squidfunk.github.io/mkdocs-material/).  We thank the contributers for this excellent open source software.

## Local Build Steps

1. Create a Python 3 conda environment called "mkdocs"
2. Add the mkdocs and mkdocs-material packages
3. Run the "mkdocs build" command
4. The site will be generated in the /site directory
5. Preview your changes with "mkdocs serve"

Sample UNIX shell script:

```sh
conda create -n mkdocs python=3
conda activate
pip install mkdocs mkdocs-material
mkdocs serve
```