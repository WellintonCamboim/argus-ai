from unittest.mock import MagicMock, patch

from argus_agent.core.agent import Agent


def test_agent_run_returns_llm_response():
    with patch("argus_agent.core.agent.ChatOpenAI") as mock_chat_openai:
        mock_llm = MagicMock()
        mock_llm.invoke.return_value = MagicMock(content="pong")
        mock_chat_openai.return_value = mock_llm

        agent = Agent()
        result = agent.run("ping")

        assert result == "pong"
        mock_llm.invoke.assert_called_once()
