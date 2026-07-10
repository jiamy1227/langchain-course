import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")

# 如果没有设置环境变量，也可以通过 api_key 参数显式传入
# todo: deepseek-v4-flash似乎不支持with_structured_output，換一個支持的模型
llm = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_API_BASE,
    temperature=0.5
    )

# 2. 定义Pydantic模型
class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

structured_llm = llm.with_structured_output(schema=CalendarEvent);

result = structured_llm.invoke("Alice and Bob are going to a science fair on Friday.")

print(result)