import pytest

from argus_agent.core.agent import Agent


def test_agent_run_not_implemented_yet():
    with pytest.raises(NotImplementedError):
        Agent().run("ping")
