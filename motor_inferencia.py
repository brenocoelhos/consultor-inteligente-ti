"""Motor de recomendação por regras para o Consultor Inteligente de Carreiras em TI."""
# Compatibilidade da biblioteca Experta com versões recentes de frozendict.
try:
    import collections.abc
    import frozendict
    if not hasattr(frozendict, "frozendict") or not hasattr(frozendict.frozendict, "__hash__"):
        pass
except Exception:
    pass

from experta import KnowledgeEngine, Fact, Rule, MATCH, P, AS

CARREIRAS = {
    "Desenvolvimento Back-end": "Construção de APIs, regras de negócio, serviços e integração com bancos de dados.",
    "Desenvolvimento Front-end & UI/UX": "Criação de interfaces responsivas, acessíveis e agradáveis de usar.",
    "Ciência de Dados e Machine Learning": "Análise estatística, descoberta de padrões e criação de modelos preditivos.",
    "Engenharia de Dados": "Organização, transformação e movimentação de dados por pipelines confiáveis.",
    "Cibersegurança": "Proteção de sistemas, análise de vulnerabilidades, redes seguras e prevenção de ataques.",
    "DevOps & SRE": "Automação, integração e entrega contínua, monitoramento e confiabilidade de serviços.",
    "Computação em Nuvem": "Planejamento e operação de infraestrutura escalável em plataformas de nuvem.",
    "Desenvolvimento Mobile": "Criação de aplicativos para dispositivos móveis, nativos ou multiplataforma.",
    "Engenharia de Qualidade e Testes (QA)": "Planejamento e automação de testes para aumentar a qualidade e a confiabilidade do software.",
    "Gestão de Produtos": "Conexão entre usuários, negócio, design e desenvolvimento, com foco em prioridades e valor."
}

class Perfil(Fact):
    """Respostas normalizadas da entrevista."""

class MotorCarreira(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.pontos = {nome: 0 for nome in CARREIRAS}
        self.motivos = {nome: [] for nome in CARREIRAS}

    def marcar(self, carreira, pontos, motivo):
        self.pontos[carreira] += pontos
        if motivo not in self.motivos[carreira]:
            self.motivos[carreira].append(motivo)

    # 25 regras cruzando preferências, ferramentas e entregas
    @Rule(Perfil(atividade="Escrever algoritmos e resolver problemas lógicos"))
    def logica_backend(self): self.marcar("Desenvolvimento Back-end", 2, "Você prefere lógica e resolução de problemas.")

    @Rule(Perfil(atividade="Criar interfaces, layouts e experiências visuais"))
    def visual_front(self): self.marcar("Desenvolvimento Front-end & UI/UX", 3, "Você demonstrou interesse por interfaces e experiência visual.")

    @Rule(Perfil(atividade="Analisar dados e encontrar padrões", matematica=P("Média") | P("Alta")))
    def dados_analise(self): self.marcar("Ciência de Dados e Machine Learning", 3, "Você gosta de analisar padrões e tem afinidade matemática média ou alta.")

    @Rule(Perfil(atividade="Organizar bancos de dados e pipelines de informação"))
    def dados_pipeline(self): self.marcar("Engenharia de Dados", 3, "Você se interessa por organização e fluxo de dados.")

    @Rule(Perfil(atividade="Investigar vulnerabilidades e proteger sistemas"))
    def cyber_atividade(self): self.marcar("Cibersegurança", 3, "Você prefere investigar vulnerabilidades e proteger sistemas.")

    @Rule(Perfil(atividade="Automatizar tarefas e manter serviços funcionando"))
    def devops_atividade(self): self.marcar("DevOps & SRE", 3, "Você gosta de automação e operação confiável.")

    @Rule(Perfil(atividade="Planejar servidores e infraestrutura em nuvem"))
    def cloud_atividade(self): self.marcar("Computação em Nuvem", 3, "Você se interessa por servidores e infraestrutura escalável.")

    @Rule(Perfil(atividade="Criar aplicativos para celulares"))
    def mobile_atividade(self): self.marcar("Desenvolvimento Mobile", 3, "Você prefere criar aplicativos para celulares.")

    @Rule(Perfil(atividade="Encontrar erros e garantir a qualidade do software"))
    def qa_atividade(self): self.marcar("Engenharia de Qualidade e Testes (QA)", 3, "Você gosta de encontrar falhas e validar software.")

    @Rule(Perfil(atividade="Organizar prioridades e conectar negócio, design e tecnologia"))
    def produto_atividade(self): self.marcar("Gestão de Produtos", 3, "Você gosta de conectar negócio, design e tecnologia.")

    @Rule(Perfil(ferramenta="Python"))
    def python_data(self): self.marcar("Ciência de Dados e Machine Learning", 1, "Python é bastante usado em análise de dados e IA.")

    @Rule(Perfil(ferramenta="Python", matematica="Alta"))
    def python_math(self): self.marcar("Ciência de Dados e Machine Learning", 2, "A combinação de Python e alta afinidade matemática favorece dados e ML.")

    @Rule(Perfil(ferramenta="JavaScript"))
    def js_front(self): self.marcar("Desenvolvimento Front-end & UI/UX", 2, "JavaScript tem forte presença no desenvolvimento web.")

    @Rule(Perfil(ferramenta="SQL e ferramentas de dados"))
    def sql_data(self): self.marcar("Engenharia de Dados", 2, "SQL e ferramentas de dados combinam com preparação e gestão de dados.")

    @Rule(Perfil(ferramenta="Linux e redes"))
    def linux_cyber(self): self.marcar("Cibersegurança", 2, "Linux e redes são conhecimentos importantes em segurança.")

    @Rule(Perfil(ferramenta="Ferramentas de testes/QA"))
    def qa_tool(self): self.marcar("Engenharia de Qualidade e Testes (QA)", 2, "Sua ferramenta de maior afinidade está ligada à qualidade.")

    @Rule(Perfil(ferramenta="Nuvem e contêineres"))
    def cloud_tool(self): self.marcar("Computação em Nuvem", 2, "Nuvem e contêineres combinam com infraestrutura moderna.")

    @Rule(Perfil(ferramenta="Nuvem e contêineres", entrega="Automação e estabilidade dos serviços"))
    def cloud_devops_cross(self): self.marcar("DevOps & SRE", 2, "Você combina ferramentas de infraestrutura com interesse em estabilidade.")

    @Rule(Perfil(ferramenta="Flutter/React Native"))
    def mobile_tool(self): self.marcar("Desenvolvimento Mobile", 2, "Flutter e React Native são usados em desenvolvimento mobile.")

    @Rule(Perfil(ferramenta="Gestão ágil e produto"))
    def product_tool(self): self.marcar("Gestão de Produtos", 2, "Sua afinidade com gestão ágil combina com planejamento de produto.")

    @Rule(Perfil(entrega="APIs, regras de negócio e serviços"))
    def backend_delivery(self): self.marcar("Desenvolvimento Back-end", 2, "Você prefere entregar APIs e serviços.")

    @Rule(Perfil(entrega="Uma interface bonita e fácil de usar"))
    def front_delivery(self): self.marcar("Desenvolvimento Front-end & UI/UX", 2, "Você valoriza interfaces simples e boas para o usuário.")

    @Rule(Perfil(entrega="Previsões, análises e modelos inteligentes", matematica=P("Média") | P("Alta")))
    def ml_delivery(self): self.marcar("Ciência de Dados e Machine Learning", 2, "Você quer trabalhar com modelos inteligentes e tem afinidade quantitativa.")

    @Rule(Perfil(entrega="Dados organizados e disponíveis para outras equipes"))
    def data_delivery(self): self.marcar("Engenharia de Dados", 2, "Você valoriza dados organizados e disponíveis para outras equipes.")

    @Rule(Perfil(entrega="Software confiável, com menos falhas"))
    def qa_delivery(self): self.marcar("Engenharia de Qualidade e Testes (QA)", 2, "Você prioriza software confiável e com menos falhas.")

    @Rule(Perfil(ambiente="Cuidando da infraestrutura e da operação"))
    def infra_environment(self): self.marcar("DevOps & SRE", 1, "Você prefere trabalhar com infraestrutura e operação.")

    @Rule(Perfil(ambiente="Testando, avaliando riscos e prevenindo problemas"))
    def qa_security_environment(self): 
        self.marcar("Engenharia de Qualidade e Testes (QA)", 1, "Seu ambiente preferido envolve testes e prevenção de problemas.")
        self.marcar("Cibersegurança", 1, "A avaliação de riscos também se relaciona à segurança.")

    @Rule(Perfil(ambiente="Planejando e tomando decisões de produto"))
    def product_environment(self): self.marcar("Gestão de Produtos", 2, "Você se identifica com planejamento e decisões de produto.")

def recomendar_carreira(matematica, atividade, ferramenta, entrega, ambiente):
    motor = MotorCarreira()
    motor.reset()
    motor.declare(Perfil(matematica=matematica, atividade=atividade, ferramenta=ferramenta,
                         entrega=entrega, ambiente=ambiente))
    motor.run()
    ranking = sorted(motor.pontos.items(), key=lambda item: item[1], reverse=True)
    melhor, pontos = ranking[0]
    motivos = motor.motivos[melhor] or ["Esta foi a trilha com maior pontuação entre as regras ativadas."]
    return {"carreira": melhor, "descricao": CARREIRAS[melhor], "motivos": motivos,
            "ranking": ranking, "pontos": pontos}
