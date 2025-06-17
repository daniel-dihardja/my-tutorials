import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from agent.types import TutorialStep, TutorialStepsList


parser = PydanticOutputParser(pydantic_object=TutorialStepsList)

llm = ChatOpenAI(model="gpt-4o")


async def refine_topic(topic: str, level: str) -> str:
    tpl = """
    You are an expert tutorial designer.

    Your task is to take the following user input and generate a **well-scoped tutorial title** and a **concise description** of what the tutorial will cover.

    🔒 Important: You are NOT creating the full tutorial or its content.  
    Your output will be used as a seed for other agents to generate the actual steps and content.

    Use the following input:
    - User input: {topic}
    - Target level: {level}

    Requirements:
    - The **title** should be clear, specific, and appropriate for a {level}-level learner.
    - The **description** should be 1–2 sentences explaining the goal and scope of the tutorial.
    - Make sure the description sets a clear boundary: what will be explained, and what prior knowledge is assumed (if any).
    - Keep it focused only on defining the tutorial’s subject, not teaching it.
    """
    prompt = PromptTemplate.from_template(tpl)
    chain = prompt | llm
    result = await chain.ainvoke({"topic": topic, "level": level})
    return result.content


async def step_planner(refined_topic: str, level: str) -> list[TutorialStep]:
    tpl = """
    You are an expert tutorial designer.

    Your task is to take the following tutorial topic and generate a step-by-step breakdown of what a learner must do to reach the learning goal.

    Tutorial topic:
    {refined_topic}

    Instructions:
    - Break the tutorial into 5 to 10 **learning steps**.
    - Each step must include:
      - A short and descriptive **title**
      - A **description** explaining what the learner will achieve or learn in that step
    - The steps should be ordered logically, with each one building on the previous.
    - Assume the learner is at a {level} level.
    - DO NOT write the content — just define the steps.

    {format_instructions}
    """

    prompt = PromptTemplate.from_template(tpl).partial(
        format_instructions=parser.get_format_instructions()
    )

    chain = prompt | llm | parser

    result: TutorialStepsList = await chain.ainvoke(
        {"refined_topic": refined_topic, "level": level}
    )

    return result.steps
