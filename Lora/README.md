# LoRA fine tuning optimizations

This is a demo comparison of LoRA fine tunings using both transformers and unsloth.


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

3 different fine-tunings were conducted and a notebook is provided for each:

|Description|Link|
|-----------|----|
|Lora fine tuning llama-3 8B using transformers library|[Lora.ipynb](./Lora.ipynb)|
|Lora fine tuning of llama-3 8B using unsloth library |[LoraUnsloth.ipynb](./LoraUnsloth.ipynb)|
|Lora fine tuning of llama-3 8B using unsloth library with optimizations|[OptimizedLoraUnsloth.ipynb](./OptimizedLoraUnsloth.ipynb)|

In each fine-tuning, we first do continual training to introduce hindi language, then do instruction fine-tuning for the model to learn answering in hindi.


## Results Comparison

- Dataset used for continual pre-training: [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) hindi
- Dataset used for instruction fine-tuning: [FreedomIntelligence/alpaca-gpt4-hindi](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-hindi)
- Each training was performed for 240 steps to keep the experiment within time and resource limits.
- Total params in the model: 8,365,805,568
- All hyperparams were kept same
- 1 RTX 4090 24GB was used for the experiments
- Note that process was restarted before each fine-tuning within each notebook to reset memory.

### Continued Pre-training Results

|Technique|Trainable Params|Total Params|Peak Reserved Memory Total(GB)|Peak Memory for Training(GB)|Peak reserved memory % of max memory|Time Taken(s)|
|---------|----------------|------------|------------------------------|----------------------------|------------------------------------|-------------|
|LoRA using transformers|335,544,320|13.945|4.601|59.569|157.5131|
|LoRA using unsloth|335,544,320|8,365,805,568|9.645|2.946|84.8644|
|LoRA using unsloth optimized|1,386,217,472|9,416,478,720

### Instruction Fine-Tuning Results


|Technique|Peak Reserved Memory Total(GB)|Peak Memory for Training(GB)|Peak reserved memory % of max memory|Time Taken(s)|
|---------|------------------------------|----------------------------|------------------------------------|-------------|
|LoRA using transformers|335,544,320|8,365,805,568|21.83|12.525|93.251|611.1513|
|LoRA using unsloth|335,544,320|8,365,805,568|11.332|4.613|48.07|596.7715|
|LoRA using unsloth optimized|1,386,217,472|9,416,478,720|21.492|11.824|91.807|672.1318|
