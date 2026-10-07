from argus_agent.core.agent import Agent


def main() -> None:
    agent = Agent()
    print(agent.run("ping"))


if __name__ == "__main__":
    main()
