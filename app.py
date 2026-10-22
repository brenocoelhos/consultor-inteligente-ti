import streamlit as st
from motor_inferencia import recomendar_carreira, CARREIRAS

st.set_page_config(page_title="Consultor de Carreiras em TI", page_icon="🧭", layout="centered")

st.title("🧭 Consultor Inteligente de Carreiras em TI")
st.write("Responda às perguntas e descubra qual trilha de tecnologia combina mais com seu perfil.")
st.caption("Projeto acadêmico de Inteligência Artificial — Sistema Especialista baseado em regras.")

with st.form("entrevista"):
    matematica = st.radio("1. Como você se sente em relação a matemática e estatística?",
                          ["Baixa", "Média", "Alta"], horizontal=True)
    atividade = st.selectbox("2. Qual atividade mais chama sua atenção?", [
        "Escrever algoritmos e resolver problemas lógicos",
        "Criar interfaces, layouts e experiências visuais",
        "Analisar dados e encontrar padrões",
        "Organizar bancos de dados e pipelines de informação",
        "Investigar vulnerabilidades e proteger sistemas",
        "Automatizar tarefas e manter serviços funcionando",
        "Planejar servidores e infraestrutura em nuvem",
        "Criar aplicativos para celulares",
        "Encontrar erros e garantir a qualidade do software",
        "Organizar prioridades e conectar negócio, design e tecnologia",
    ])
    ferramenta = st.selectbox("3. Qual linguagem ou ferramenta você tem mais afinidade?", [
        "Python", "JavaScript", "SQL e ferramentas de dados", "Linux e redes",
        "Ferramentas de testes/QA", "Nuvem e contêineres", "Flutter/React Native",
        "Gestão ágil e produto", "Nenhuma / estou começando"
    ])
    entrega = st.selectbox("4. Que tipo de resultado você prefere entregar?", [
        "APIs, regras de negócio e serviços",
        "Uma interface bonita e fácil de usar",
        "Previsões, análises e modelos inteligentes",
        "Dados organizados e disponíveis para outras equipes",
        "Sistemas mais seguros",
        "Automação e estabilidade dos serviços",
        "Infraestrutura escalável e confiável",
        "Um aplicativo móvel funcional",
        "Software confiável, com menos falhas",
        "Um produto alinhado às necessidades dos usuários",
    ])
    ambiente = st.radio("5. Em qual ambiente você gostaria de trabalhar?", [
        "Programando e resolvendo desafios técnicos",
        "Criando e melhorando experiências para pessoas",
        "Investigando informações e padrões",
        "Cuidando da infraestrutura e da operação",
        "Testando, avaliando riscos e prevenindo problemas",
        "Planejando e tomando decisões de produto",
    ])
    enviar = st.form_submit_button("Descobrir minha trilha", type="primary", use_container_width=True)

if enviar:
    resultado = recomendar_carreira(matematica, atividade, ferramenta, entrega, ambiente)
    st.success(f"Trilha recomendada: **{resultado['carreira']}**")
    st.subheader("Por que essa trilha?")
    st.write(resultado["descricao"])
    st.markdown("**Principais motivos identificados:**")
    for motivo in resultado["motivos"]:
        st.write(f"- {motivo}")
    with st.expander("Ver outras trilhas consideradas"):
        for nome, pontos in resultado["ranking"][1:]:
            st.write(f"**{nome}** — {pontos} ponto(s)")
    st.info("A recomendação é uma orientação inicial baseada nas respostas, não uma decisão definitiva sobre sua carreira.")

st.divider()
st.caption("Desenvolvido em Python com motor de regras Experta e interface Streamlit.")
