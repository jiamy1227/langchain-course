# uv add langchain-ollama
from langchain_ollama import ChatOllama

# 基本用法
ollama_llm = ChatOllama(model="qwen3:4b",  base_url="http://localhost:11434")
print(ollama_llm.profile)
# response = ollama_llm.invoke("你好，介绍一下你自己")
# print(response.content)