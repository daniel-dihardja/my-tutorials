# subgraphs/research_subgraph.py

from langgraph.graph import StateGraph
from langchain_core.runnables import Runnable

from agent.types import State
from agent.subgraphs.llm_chains import refine_topic


# Example node
async def main(state: State) -> State:
    state.refined_topic = await refine_topic(state.topic, state.level)
    return state


def build_topic_refiner_agent() -> Runnable:
    graph = StateGraph(State)
    graph.add_node("main", main)
    graph.set_entry_point("main")
    return graph.compile()
