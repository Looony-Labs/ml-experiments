# RAG with txtai and qdrant

This is a demo of RAG search using txtai and qdrant as the vector store.


## Setting up the environment

For this demo you need:
- docker (or qdrant server running remotely and config can be changed accordingly)
- conda (can follow the steps [from here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html))

The best way to get started is to set up the environment using conda

First, install conda, then install all deps:

```
conda env create -f environment.yml
```

Activate the env

```
conda activate llm_exp_rag
```

Start the Qdrant server. If running via docker, it can be done by

```
docker run -p 6333:6333 -p:6334:6334 qdrant/qdrant:v1.7.1
```

Finally, launch ```jupyter-lab``` and navigate to ```RAG_exp.ipynb``` notebook

```
jupyter-lab
```

