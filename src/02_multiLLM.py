from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()

# 一个函数搞定所有提供商，通过 model_provider 参数区分
llm_deepseek = init_chat_model("deepseek-v4-flash", model_provider="openai",api_key=os.getenv("DEEPSEEK_API_KEY"),base_url=os.getenv("DEEPSEEK_API_BASE"))
llm_gemini = init_chat_model("gemini-1.5-flash", model_provider="google_genai",api_key=os.getenv("GEMINI_API_KEY"),base_url=os.getenv("GEMINI_BASE_URL"))

# 调用方式完全一致
for name, llm in [("DeepSeek", llm_deepseek), ("Gemini", llm_gemini)]:
    response = llm.invoke("用一句话介绍你自己")
    print(f"{name}: {response.content}")