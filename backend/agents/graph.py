from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from agents.state import AgentState
from agents.llm_agent import llm
from agents.tools import (
    sql_tool,
    rag_tool,
    forecast_tool,
    anomaly_tool,
)

# Register all tools
tools = [
    sql_tool,
    rag_tool,
    forecast_tool,
    anomaly_tool,
]

# Bind tools to Gemini
llm_with_tools = llm.bind_tools(tools)


# -------------------------
# LLM Node
# -------------------------
def chatbot(state: AgentState):
    """
    Calls Gemini.
    Gemini decides whether to answer directly
    or call one of the tools.
    """

    return {
        "messages": [
            llm_with_tools.invoke(state["messages"])
        ]
    }


# -------------------------
# Tool Node
# -------------------------
tool_node = ToolNode(tools)


# -------------------------
# Build Graph
# -------------------------
graph_builder = StateGraph(AgentState)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

graph_builder.add_edge("tools", "chatbot")

graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()