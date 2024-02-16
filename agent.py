import boto3
from langchain.llms.bedrock import Bedrock

from dotenv import dotenv_values
secrets= dotenv_values(".env")


from langchain.tools import DuckDuckGoSearchRun

from langchain import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


from langchain.agents import Tool
from langchain.tools import BaseTool


from langchain.agents import initialize_agent
from tools import tool_call as ts


import db_helper as dh

llm = Bedrock(
    client= boto3.client(
    service_name="bedrock-runtime",
    aws_access_key_id = secrets["aws_access_key_id"],
    aws_secret_access_key = secrets["aws_secret_access_key"],
    region_name="us-east-1",
    ),
    model_id="anthropic.claude-instant-v1", 
    model_kwargs={
                "max_tokens_to_sample":8000,
                "temperature": 0,
                # "top_p": 1,
                # "top_k": 250,
                "anthropic_version": "bedrock-2023-05-31"
                },
    
    )

search = DuckDuckGoSearchRun()
# defining a single tool
tools = [
    Tool(
        name = "search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    )
]


tools = [ ts.gruppi, ts.risorse, ts.permessi_wr, ts.query, ts.eventi]

# conversational agent memory
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=3,
    return_messages=True
)


# create our agent
conversational_agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=4,
    early_stopping_method='generate',
    memory=memory
)


def ask_llm(input_str):
   return conversational_agent(str(input_str))['output']


# print(ask_llm("dammi i primi 10 gruppi?"))



