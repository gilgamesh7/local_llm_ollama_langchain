from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

print(llm.invoke("Tell me all about Goddess Renuka Devi"))

