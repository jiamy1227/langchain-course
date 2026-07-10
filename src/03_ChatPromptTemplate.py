from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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


chat_prompt1 = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的{role}。"),
    ("human", "请回答关于{topic}的问题。"),
    ("ai", "好的，我会尽力回答。"),
    ("human", "{question}")
])

# 调用模板，生成消息列表
messages = chat_prompt1.invoke({
    "role": "Python编程助手",
    "topic": "Python装饰器",
    "question": "什么是装饰器？"
})
print(messages)


chat_prompt2 = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个有帮助的AI助手"),    # 固定内容用Message对象
    HumanMessage(content="你好！"),                     # 固定内容
    AIMessage(content="你好！有什么可以帮助你的？"),      # 固定内容
    ("human", "请介绍{topic}")                          # 含变量的用元组形式
])

messages2 = chat_prompt2.invoke({"topic": "LangChain"})


# print(llm.invoke(messages2))

for chunk in llm.stream(messages2):
    print(chunk.content, end="", flush=True)