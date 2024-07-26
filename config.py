# OPENAI_API_URL = 'https://open.bigmodel.cn/api/paas/v4/'
OPENAI_API_URL = 'http://localhost:11524/v1'
OPENAI_API_KEY = 'bce70f907a7e4f878c0fa02050822690.oUdZnbFXE3jOjY3n'
# MODEL_NAME = "glm-4"
MODEL_NAME = "local_model"
LLM_CONFIG = {"config_list": [
    {"model": MODEL_NAME, "api_key": OPENAI_API_KEY, 'base_url': OPENAI_API_URL},
]}
