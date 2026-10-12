from langchain_openai import ChatOpenAI

from argus_agent.config import settings
from argus_agent.prompts.system import SYSTEM_PROMPT


class Agent:
    def __init__(self) -> None:
        self._llm = ChatOpenAI(
            model=settings.openrouter_model,
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.openrouter_api_key,
        )

    def run(self, question: str) -> str:
        messages = []
        if SYSTEM_PROMPT:
            messages.append(("system", SYSTEM_PROMPT))
        messages.append(("human", question))

        response = self._llm.invoke(messages)
        return response.content
