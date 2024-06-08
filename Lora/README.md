# LoRA fine tuning optimizations

This is a demo of LoRA fine tunings using both transformers and unsloth.


## Setting up the environment

For this demo you need:
- conda (can follow the steps [from here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html))
- 24G GPU access.

The best way to get started is to set up the environment using conda

First, install conda, then install all deps:

```
conda env create -f environment.yml
```

Activate the env

```
conda activate llm_exp_lora
```

Finally, launch ```jupyter-lab``` and navigate to ```Lora.ipynb``` notebook

```
jupyter-lab
```

### Fine-Tuning

Following fine-tuning notebooks are provided

|Description|Link|
|-----------|----|
|Lora fine tuning llama-3 8B using transformers|[Lora.ipynb](./Lora.ipynb)|
|Lora fine tuning of llama-3 8B using unsloth|[LoraUnsloth.ipynb](./LoraUnsloth.ipynb)|
|Lora fine tuning of llama-3 8B using unsloth with optimizations|[OptimizedLoraUnsloth.ipynb](./OptimizedLoraUnsloth.ipynb)|
