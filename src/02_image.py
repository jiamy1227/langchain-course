import os
import base64
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

# 基本用法
ollama_llm = ChatOllama(model="qwen3.5:4b",  base_url="http://localhost:5307")
print(ollama_llm.profile)

# 读取图片
with open("static/car.jpeg", "rb") as f:
    image_data = f.read()

message = HumanMessage(content=[
    {"type": "text", "text": "描述这张图片"},
    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode()}"}}
])


# type:image_url :既支持远程可以访问的图片地址 也支持本地图片(不能把本地图片路径丢给它 本地图片内容)
#response = ollama_llm.invoke([message])
response = ollama_llm.invoke("用一句话介绍你自己")
print(response.content)

