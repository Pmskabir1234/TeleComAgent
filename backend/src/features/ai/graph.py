from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage
from .nodes import route_query
from .experts import handle_billing, handle_network, handle_general

class AgentState(TypedDict):
    # Using a list for messages to maintain conversation history
    messages: Annotated[list[BaseMessage], "The history of the conversation"]
    routing_decision: str
    context: str

def create_agent_graph():
    # Initialize the graph with our state
    workflow = StateGraph(AgentState)

    # Add the nodes
    workflow.add_node("router", route_query)
    workflow.add_node("billing_expert", handle_billing)
    workflow.add_node("network_expert", handle_network)
    workflow.add_node("general_expert", handle_general)

    # Set the entry point
    workflow.set_entry_point("router")

    # Define conditional edges based on the router's decision
    workflow.add_conditional_edges(
        "router",
        lambda x: x["routing_decision"],
        {
            "billing": "billing_expert",
            "network": "network_expert",
            "general": "general_expert"
        }
    )

    # All experts lead to the end of the turn
    workflow.add_edge("billing_expert", END)
    workflow.add_edge("network_expert", END)
    workflow.add_edge("general_expert", END)

    return workflow.compile()
