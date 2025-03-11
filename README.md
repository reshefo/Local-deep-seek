# Local-DeepSeek

This repository provides instructions for running the DeepSeek 1.5B parameters version locally.

## Setup Instructions

1. Download the following files from the DeepSeek model repository: 
   https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B/tree/main
   
   Required files:
   - config.json
   - generation_config.json
   - model.safetensors
   - tokenizer.json
   - tokenizer_config.json

2. Save all files in a specific directory (in the fallowing code it called "model_path").

Note: Using the .safetensors format instead of pickle files is recommended for security reasons.

3. save your excel data in "data_path".
