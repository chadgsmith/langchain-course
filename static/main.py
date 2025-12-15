from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
#imports the tool decrator
from langchain.tools import tool
#human message is used to invoke the agent
from langchain_core.messages import HumanMessage
from langchain_openai import OpenAI, ChatOpenAI
from langchain_tavily import TavilySearch







llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from static!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an AI engineer in the langchain in the bay area in linked in and list their details")})
    print(result)



if __name__ == "__main__":
    main()
