# Argus Agent

Agente de suporte que analisa documentação de projetos, consulta Grafana/logs
e bancos de dados para investigar bugs e responder dúvidas de clientes.

## Setup

```bash
cp .env.example .env   # preencher as credenciais
pip install -e ".[dev]"
```

## Estrutura

```
src/argus_agent/
  config.py       # configuração (variáveis de ambiente)
  core/agent.py   # orquestração do agente (loop, decisão de tools)
  tools/          # ferramentas que o agente pode chamar
    grafana.py    # consulta métricas/logs no Grafana
    database.py   # consulta nos bancos de dados monitorados
    docs.py       # busca na documentação dos projetos
  prompts/        # prompts de sistema do agente
  main.py         # ponto de entrada
tests/
```

## Rodar

```bash
python -m argus_agent.main
```
