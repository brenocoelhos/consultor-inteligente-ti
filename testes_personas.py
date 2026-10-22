"""Testes básicos das quatro personas descritas no enunciado."""
from motor_inferencia import recomendar_carreira

PERSONAS = [
    {
        "nome": "Analítico",
        "respostas": ("Alta", "Analisar dados e encontrar padrões", "Python",
                      "Previsões, análises e modelos inteligentes", "Investigando informações e padrões"),
        "esperada": "Ciência de Dados e Machine Learning",
    },
    {
        "nome": "Visual / Front-end",
        "respostas": ("Média", "Criar interfaces, layouts e experiências visuais", "JavaScript",
                      "Uma interface bonita e fácil de usar", "Criando e melhorando experiências para pessoas"),
        "esperada": "Desenvolvimento Front-end & UI/UX",
    },
    {
        "nome": "Infraestrutura / Segurança",
        "respostas": ("Média", "Investigar vulnerabilidades e proteger sistemas", "Linux e redes",
                      "Sistemas mais seguros", "Testando, avaliando riscos e prevenindo problemas"),
        "esperada": "Cibersegurança",
    },
    {
        "nome": "Qualidade",
        "respostas": ("Baixa", "Encontrar erros e garantir a qualidade do software", "Ferramentas de testes/QA",
                      "Software confiável, com menos falhas", "Testando, avaliando riscos e prevenindo problemas"),
        "esperada": "Engenharia de Qualidade e Testes (QA)",
    },
]

if __name__ == "__main__":
    for persona in PERSONAS:
        r = recomendar_carreira(*persona["respostas"])
        status = "OK" if r["carreira"] == persona["esperada"] else "REVISAR"
        print(f'{persona["nome"]}: {r["carreira"]} — esperado: {persona["esperada"]} [{status}]')
