from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from agent.types import State

from agent.subgraphs.topic_refiner_agent import build_topic_refiner_agent
from agent.subgraphs.step_planer_agent import build_step_planer_agent


# Define the graph
graph = (
    StateGraph(State)
    .add_node("refine_topic", build_topic_refiner_agent())
    .add_node("step_planer", build_step_planer_agent())
    .add_edge("__start__", "refine_topic")
    .add_edge("refine_topic", "step_planer")
    .add_edge("step_planer", "__end__")
    .compile(name="New Graph")
)
