import boto3
from langchain.llms.bedrock import Bedrock

from dotenv import dotenv_values
secrets= dotenv_values(".env")



from langchain.chains.conversation.memory import ConversationBufferWindowMemory


from langchain.agents import Tool
from langchain.tools import BaseTool


from langchain.agents import initialize_agent

llm = Bedrock(
    client= boto3.client(
    service_name="bedrock-runtime",
    aws_access_key_id = secrets["aws_access_key_id"],
    aws_secret_access_key = secrets["aws_secret_access_key"],
    region_name="us-east-1",
    ),
    model_id="anthropic.claude-v2", 
    model_kwargs={
                "max_tokens_to_sample":8000,
                "temperature": 0,
                # "top_p": 1,
                # "top_k": 250,
                "anthropic_version": "bedrock-2023-05-31"
                },
    
    )






import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI


#llm = OpenAI(api_token="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")

df = SmartDataframe("users.csv", config={"llm": llm})
# response = df.chat(
#     "Dammi tutti gli email che iniziano con la lettera 'al'. Skip tutti quelli che sono null. Una volta dato la risposta come tabella, fai un plot",
#     #"Give me info about PELLEGRINI ALESSAN user",
# )
while True:
    response = df.chat(
    str(input("\n\n\n Ask me everything: \n\n\n"))
    )

#Print the rows with name that starts with 'A' then, give me a plot with the 'ID' and 'NOMINATIVO' from the content.


    print(response) 



print("ok")