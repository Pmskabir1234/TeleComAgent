from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from .llm import get_llm
from .graph import AgentState

def handle_billing(state: AgentState):
    """Expert node for billing and account queries."""
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Telecom Billing Expert. Help the user with billing, payments, and account charges. Be concise, professional, and transparent."),
        ("user", "{query}")
    ])
    chain = prompt | llm
    user_query = state["messages"][-1].content if state["messages"] else ""
    response = chain.invoke({"query": user_query})
    return {"messages": [response]}

def handle_network(state: AgentState):
    """Expert node for network and connectivity queries."""
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a Telecom Network Engineer. Help the user with internet connectivity, SIM issues, and signal problems. Provide step-by-step troubleshooting."),
        ("user", "{query}")
    ])
    chain = prompt | llm
    user_query = state["messages"][-1].content if state["messages"] else ""
    response = chain.invoke({"query": user_query})
    return {"messages": [response]}

def handle_general(state: AgentState):
    """Expert node for general inquiries and company info."""
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a friendly Telecom Assistant. Answer general questions about plans, services, and company policies."),
        ("user", "{query}")
    ])
    chain = prompt | llm
    user_query = state["messages"][-1].content if state["messages"] else ""
    response = chain.invoke({"query": user_query})
    return {"messages": [response]}
