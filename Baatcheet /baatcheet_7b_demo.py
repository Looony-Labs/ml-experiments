# -*- coding: utf-8 -*-
"""Baatcheet-7b-demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KAWiCFF7yLaNFcyDUjVr0ci_TRTanZax
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# import torch
# major_version, minor_version = torch.cuda.get_device_capability()
# # Must install separately since Colab has torch 2.2.1, which breaks packages
# !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
# if major_version >= 8:
#     # Use this for new GPUs like Ampere, Hopper GPUs (RTX 30xx, RTX 40xx, A100, H100, L40)
#     !pip install --no-deps packaging ninja einops flash-attn xformers trl peft accelerate bitsandbytes
# else:
#     # Use this for older GPUs (V100, Tesla T4, RTX 20xx)
#     !pip install --no-deps xformers trl peft accelerate bitsandbytes
# pass

from unsloth import FastLanguageModel
import torch
max_seq_length = 2048 # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

model_baatcheet, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "fnnerd/Baatcheet-7b", # Choose ANY! eg teknium/OpenHermes-2.5-Mistral-7B
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)

prompt = "Translation ### English:'You don't know the movie Sholey?? Such an iconic movie! And I love the character Gabbar. How nicely crafted.' to ### Hinglish: "

inputs = tokenizer([prompt], return_tensors = "pt").to("cuda")
outputs = model_baatcheet.generate(**inputs, max_new_tokens = 64)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))

prompt = "Translation ### English:''Which character from 'Lord of the Rings' is your favorite?'' to ### Hinglish: "

inputs = tokenizer([prompt], return_tensors = "pt").to("cuda")
outputs = model_baatcheet.generate(**inputs, max_new_tokens = 64)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))