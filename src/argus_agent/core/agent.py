# Orquestração do agente: monta o prompt, decide quais tools chamar e conduz
# o loop de conversa com o modelo. Implementaremos isso nos próximos passos.


class Agent:
    def run(self, question: str) -> str:
        raise NotImplementedError
