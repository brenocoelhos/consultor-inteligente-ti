# Consultor Inteligente de Carreiras em TI

Projeto acadêmico para a disciplina de Inteligência Artificial. O sistema entrevista o usuário e recomenda uma entre dez trilhas de carreira em Tecnologia da Informação usando um conjunto de regras e uma interface web.

## Trilhas disponíveis
1. Desenvolvimento Back-end
2. Desenvolvimento Front-end & UI/UX
3. Ciência de Dados e Machine Learning
4. Engenharia de Dados
5. Cibersegurança
6. DevOps & SRE
7. Computação em Nuvem
8. Desenvolvimento Mobile
9. Engenharia de Qualidade e Testes (QA)
10. Gestão de Produtos

## Tecnologias
- Python 3.10
- Experta (motor de regras)
- Streamlit (interface web)

## Executar localmente
Recomenda-se Python 3.10 em ambiente virtual.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Publicar
1. Envie todos os arquivos deste projeto para um repositório no GitHub.
2. Acesse https://share.streamlit.io/ e entre com sua conta.
3. Escolha **Create app**, selecione o repositório, a branch e o arquivo `app.py`.
4. Clique em **Deploy**.

## Como funciona
As respostas da entrevista são enviadas ao motor de inferência. Regras SE–ENTÃO atribuem pontos às trilhas relacionadas ao perfil. A trilha com maior pontuação é exibida junto de uma justificativa e do ranking das demais opções.

## Personas sugeridas para validação
- **Perfil analítico:** alta afinidade matemática, interesse em analisar padrões e entrega de modelos inteligentes.
- **Perfil visual:** interesse em layouts, JavaScript e interfaces fáceis de usar.
- **Perfil infraestrutura/segurança:** interesse em Linux/redes, proteção de sistemas e prevenção de riscos.
- **Perfil qualidade:** interesse em encontrar erros, ferramentas de QA e software confiável.

## Observação acadêmica
Revise as regras e execute testes antes da entrega. As pontuações são uma heurística didática e podem ser ajustadas para melhorar a diferenciação entre trilhas próximas.
