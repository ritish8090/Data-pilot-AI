from typing import Annotated

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """
    State shared across the LangGraph workflow.
    """

    messages: Annotated[list[BaseMessage], add_messages]