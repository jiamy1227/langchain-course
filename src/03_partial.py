from langchain_core.prompts import PromptTemplate

#####partial：预先设置部分参数###########

prompt1 = PromptTemplate.from_template("讲一个关于{topic}的{adjective}故事")

fixed_prompt1 = prompt1.partial(adjective="有趣")  # 预先设置形容词参数为“有趣”
print(fixed_prompt1.format(topic="猫"))  # 输出: 讲一个关于猫的有趣故事

prompt2 = PromptTemplate(
    input_variables=["topic"],
    template="讲一个关于{topic}的{adjective}故事",
    partial_variables={"adjective": "感人"}  # 预先设置形容词参数为“感人”
)
print(prompt2.invoke({"topic": "狗"}))  # 输出: 讲一个关于狗的感人故事