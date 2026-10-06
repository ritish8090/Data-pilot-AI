from langchain_core.messages import HumanMessage

from agents.graph import graph

response = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Who are the top 5 customers by sales?"
            )
        ]
    }
)

print("\n========================\n")

for message in response["messages"]:
    print(message)