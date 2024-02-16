import agent


def hello(in_on):
 resp = agent.ask_llm(in_on)
 print(resp)
 return str(resp)