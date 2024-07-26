#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen2-72B-Instruct-GPTQ-Int8', cache_dir="./models/")