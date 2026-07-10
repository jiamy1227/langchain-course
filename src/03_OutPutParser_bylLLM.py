import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

class Prime(BaseModel):
    prime: list[int] = Field(description="素数")
    count: list[int] = Field(description="小于该素数的素数个数")


load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")

# 如果没有设置环境变量，也可以通过 api_key 参数显式传入
llm = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_API_BASE,
    temperature=0.5
    )

json_parser = JsonOutputParser(pydantic_object=Prime)


res = llm.invoke([
    ("system",json_parser.get_format_instructions()),
    ("user", "任意生成5个1000-100000之间的素数，并标出小于该素数的素数个数")
])

# print(res.content)

# JsonOutputParser：在系統提示詞中自動加入model的格式說明
print(json_parser.get_format_instructions())