import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    HumanMessage,SystemMessage,AIMessage
)
import asyncio


load_dotenv()

# 一个函数搞定所有提供商，通过 model_provider 参数区分
llm_deepseek = init_chat_model("gpt-5.4-nano-2026-03-17", model_provider="openai",api_key=os.getenv("DEEPSEEK_API_KEY"),base_url=os.getenv("DEEPSEEK_API_BASE"))
llm_gemini = init_chat_model("gemini-3.1-flash-lite-preview", model_provider="google_genai",api_key=os.getenv("GEMINI_API_KEY"),base_url=os.getenv("GEMINI_BASE_URL"))

# 调用方式完全一致
for name, llm in [("OpenAI", llm_deepseek), ("Claude", llm_claude), ("Gemini", llm_gemini)]:
    response = llm.invoke("用一句话介绍你自己")
    print(f"{name}: {response.content}")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")



# async def call_llm_async():
#     response = await llm.ainvoke("什么是LangChain？")
#     print(response.content)

# # Jupyter Notebook 中直接 await（见下方说明）
# asyncio.run(call_llm_async()) # 方式二  
print(llm.profile)
