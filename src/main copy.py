import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    HumanMessage,SystemMessage,AIMessage
)
import asyncio


load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")

# 如果没有设置环境变量，也可以通过 api_key 参数显式传入
llm = ChatOpenAI(
    model="deepseek-v4-flash",
    OPENAI_API_KEY=DEEPSEEK_API_KEY,
    OPENAI_API_BASE=DEEPSEEK_API_BASE,
    temperature=0.5,
    max_retries=2,
)


# async def call_llm_async():
#     response = await llm.ainvoke("什么是LangChain？")
#     print(response.content)

# # Jupyter Notebook 中直接 await（见下方说明）
# asyncio.run(call_llm_async()) # 方式二  
print(llm.profile)
