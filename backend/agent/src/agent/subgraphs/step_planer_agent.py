# subgraphs/research_subgraph.py

from langgraph.graph import StateGraph
from langchain_core.runnables import Runnable
from agent.types import State, TutorialStep
from agent.subgraphs.llm_chains import step_planer


async def main(state: State) -> State:
    state.steps = await step_planer(state.refined_topic, state.level)
    return state


def build_step_planer_agent() -> Runnable:
    graph = StateGraph(State)
    graph.add_node("main", main)
    graph.set_entry_point("main")
    return graph.compile()
