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
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_API_BASE,
    temperature=0.5,
    max_retries=2,
)

async def batch_async():
    questions = [
        "什么是LangChain？",
        "LangChain的核心组件有哪些？",
        "如何使用LangChain构建Agent？"
    ]
    responses = await llm.abatch(questions)
    for q, r in zip(questions, responses):
        print(f"Q: {q}\nA: {r.content}\n")

if __name__ == "__main__":
    asyncio.run(batch_async())