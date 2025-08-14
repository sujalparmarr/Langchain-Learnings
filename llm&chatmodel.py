#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is LLM
from langchain_openai import OpenAI
llm = OpenAI(model="gpt-3.5-turbo-instruct")
response = llm("The capital of France is")
print(response) 

# This is CHAT MODEL
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(model="gpt-4")
response = chat_model.invoke("What is the capital of France?")
print(response.content)

