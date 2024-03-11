# -*- coding: utf-8 -*-
# Author: Mr.Jack _ www.BICweb.vn
# Start: 03Mar2024 - 09PM
# End: 11Mar2024 - 12PM

from langchain.agents import AgentExecutor, create_react_agent, load_tools
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

from langchain_community.llms import Ollama
model_local = Ollama(model='mistral')

from simple_langchain_tools import get_all_tools

tools = get_all_tools()

from langchain import hub
prompt = hub.pull("hwchase17/react-chat")

chat_history_memory = ConversationBufferWindowMemory(k=3, memory_key='chat_history', input_key='input', ouput_key='output')

agent = create_react_agent(model_local, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=chat_history_memory,
    verbose=True, # ~> Speech out the thinking
    handle_parsing_errors=True,
    )

user_input =""
while user_input != 'exit!':
    user_input = input('\n(type exit! to quit) Ask > ')
    if user_input != 'exit!':
        response = agent_executor.invoke({"input": user_input})

        print("\n")
        # print(response)
        print("Question:",response['input'])
        print("Answer:",response['output'])
        print("\n")
