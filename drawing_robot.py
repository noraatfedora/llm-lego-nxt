from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, PromptTemplate

load_dotenv()

chat = ChatOpenAI(model_name="gpt-4")

f = open("prompt_template.txt", "r")

lines = f.readlines()
template = PromptTemplate.from_template('\n'.join(lines))

shape = input("what shape should the robot draw?")
output = chat.predict(template.format(shape=shape))

print(output)
