from pydantic import BaseModel
from typing import Optional
from langchain.output_parsers import PydanticOutputParser


class TutorialStep(BaseModel):
    title: str
    description: str


class TutorialStepsList(BaseModel):
    steps: list[TutorialStep]


parser = PydanticOutputParser(pydantic_object=TutorialStepsList)


class State(BaseModel):
    topic: str = (
        "i want to learn how to setup a monorepo in turbo repo using react remix, tailwind and shadcn."
    )
    level: str = "beginner"
    refined_topic: Optional[str] = None
    steps: Optional[list[TutorialStep]] = None
