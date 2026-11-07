from typing import Literal
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from .llm import get_llm
from .graph import AgentState

def route_query(state: AgentState):
    """
    Analyzes the user query and routes it to the appropriate expert node.
    This is the first node in the graph.
    """
    llm = get_llm()

    # We use a very strict prompt to ensure the LLM only returns one of the keywords.
    # This minimizes tokens and prevents parsing errors.
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a telecom routing agent. Your only job is to classify the user's query into one of three categories: 'billing', 'network', or 'general'. Respond with ONLY the category name."),
        ("user", "{query}")
    ])

    chain = prompt | llm

    # We only need the last message in the state as the query
    user_query = state["messages"][-1].content if state["messages"] else ""

    try:
        response = chain.invoke({"query": user_query})
        decision = response.content.strip().lower()

        # Validate decision to avoid graph crashes
        if decision not in ["billing", "network", "general"]:
            decision = "general"

        return {"routing_decision": decision}
    except Exception as e:
        print(f"Routing error: {e}")
        return {"routing_decision": "general"}
