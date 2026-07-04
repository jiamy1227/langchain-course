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


# async def call_llm_async():
#     response = await llm.ainvoke("什么是LangChain？")
#     print(response.content)

# # Jupyter Notebook 中直接 await（见下方说明）
# asyncio.run(call_llm_async()) # 方式二  
#for chunk in llm.stream("什么是LangChain？"):
    # 累积消息块
    # full_message = chunk if full_message is None else full_message + chunk
    #print(chunk.content, end="", flush=True)

# 流式event
async def stream_events():
    async for event in llm.astream_events("你好"):
        if event["event"] == "on_chat_model_start":
            print(f"输入: {event['data']['input']}")
        elif event["event"] == "on_chat_model_stream":
            print(f"Token: {event['data']['chunk'].content}", end="",flush=True)
        elif event["event"] == "on_chat_model_end":
            print(f"\n做一些完成后的处理!")

if __name__ == "__main__":
    asyncio.run(stream_events())
    