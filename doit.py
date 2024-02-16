

from langchain import hub
from langchain.agents import AgentExecutor, create_xml_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from tools import tool_call as ts

import boto3
from langchain.llms.bedrock import Bedrock
from dotenv import dotenv_values
secrets= dotenv_values(".env")

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
    ), ts.anagrafica
]



# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/xml-agent-convo")


agent = create_xml_agent(llm, tools, prompt)



memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=3,
    return_messages=True
)
# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory )




def ask(input_str=""):
    response = agent_executor.invoke(
        {
            "input": input_str + " Only use a tool if needed, otherwise respond with Final Answer"
            }
    )
    return str(response['output'])

# while True:
#     input_str = str(input("Ask me something: "))
#     response = agent_executor.invoke(
#         {
#             "input": input_str + " Only use a tool if needed, otherwise respond with Final Answer"
#             }
#     )
#     print(str(response['output']))




if __name__ == "__main__":
    # This will store the conversation history
    
    while True:
        conversation_history = []