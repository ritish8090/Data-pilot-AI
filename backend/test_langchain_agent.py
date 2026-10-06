from agents.langchain_agent import agent

response = agent.invoke(
    {
        "input": "Who are the top 5 customers by sales?"
    }
)

print(response)