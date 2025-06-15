from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLL(model="llama3.2")

template = """

You are a expert in answering questions about 

Here are some relevant:  
"""