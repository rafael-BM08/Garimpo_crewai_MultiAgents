# Garimpo Afiliado

Sistema multiagente desenvolvido com CrewAI para garimpo e análise de produtos em alta para marketing de afiliados, com geração automatizada de estratégias de divulgação para redes sociais.

## Sobre o Projeto

O **Garimpo Afiliado** automatiza o processo de pesquisa e seleção de produtos para afiliados nas plataformas Shopee, Amazon e Mercado Livre.

A aplicação realiza buscas web em tempo real através da ferramenta Tavily, identifica 8 produtos em alta com base na categoria informada, avalia e ranqueia os 3 melhores produtos segundo critérios de demanda, potencial de comissão e engajamento, e gera estratégias completas de divulgação para TikTok, Pinterest e Instagram.

## Funcionalidades

- **Pesquisa web em tempo real**: Coleta de 8 produtos em alta no último mês nas plataformas suportadas (`shopee`, `amazon` ou `mercado livre`), priorizando preços e justificativas reais de alta procura.
- **Avaliação e ranking (Top 3)**: Seleção dos 3 produtos mais promissores, com atribuição de nota de 0 a 10 e justificativa detalhada.
- **Estratégias de conteúdo para redes sociais**:
  - **TikTok**: 2 estratégias por produto (título para leads, descrição de vídeo e hashtags).
  - **Pinterest**: 2 estratégias por produto (título para leads, descrição de imagem e hashtags).
  - **Instagram**: 2 estratégias por produto (título para leads, descrição de vídeo e hashtags).
- **Validação com schemas Pydantic**: Garantia de integridade e formatação padronizada em todas as etapas da Crew.
- **Exportação automática de resultados**: Persistência dos dados de cada execução em arquivos `.json` e `.md` na pasta `resultados/`.

## Tecnologias Utilizadas

- **Python** (>= 3.10, < 3.14)
- **CrewAI**: Orquestração do fluxo multiagente sequencial
- **OpenAI (`gpt-4o-mini`)**: Modelo de linguagem utilizado pelos agentes
- **Tavily Search API (`tavily-python`)**: Busca web em tempo real via `TavilySearchTool`
- **Pydantic**: Validação de dados e estruturação das saídas dos agentes
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## Como Funciona

A aplicação utiliza um processo sequencial (`Process.sequential`) onde a saída de uma etapa serve de contexto para as seguintes:

```text
Usuário (Plataforma + Categoria)
   ↓
[Agente] pesquisar_produtos (TavilySearchTool)
   → Localiza 8 produtos em alta na plataforma selecionada
   ↓
[Agente] avaliador_produtos
   → Analisa os 8 produtos e ranqueia o Top 3 com notas de 0 a 10
   ↓
[Agente] marketing_digital
   → Cria 6 estratégias para TikTok (2 por produto)
   → Cria 6 estratégias para Pinterest (2 por produto)
   → Cria 6 estratégias para Instagram (2 por produto)
   ↓
[Módulo] salvar_resultado
   → Salva resultados/<plataforma>_AAAA-MM-DD_HH-MM.json e .md
```

## Estrutura do Projeto

```text
garimpo_afiliado/
├── src/
│   └── garimpo_afiliado/
│       ├── config/
│       │   ├── agents.yaml      # Definição de roles, goals, backstories e LLMs dos agentes
│       │   └── tasks.yaml       # Definição e instruções das tarefas
│       ├── crew.py              # Definição da classe GarimpoAfiliado, agentes e tarefas
│       ├── main.py              # CLI interativa para seleção de plataforma e categoria
│       ├── models.py            # Modelos Pydantic (Produto, Top3, EstrategiasRede)
│       └── salvar.py            # Exportação das saídas em formatos JSON e Markdown
├── resultados/                  # Arquivos gerados pelas execuções
├── pyproject.toml               # Configurações de empacotamento e dependências
└── .env                         # Chaves de API e variáveis de ambiente (não versionado)
```

## Requisitos

- Python >= 3.10 e < 3.14
- Chave de API da OpenAI
- Chave de API da Tavily Search

## Configuração

Crie um arquivo `.env` dentro do diretório `garimpo_afiliado/` com as seguintes variáveis:

```env
MODEL=gpt-4o-mini
OPENAI_API_KEY="sua_chave_openai_aqui"
TAVILY_API_KEY="sua_chave_tavily_aqui"
CREWAI_TRACING_ENABLED=false
```

## Instalação

Navegue até a pasta do projeto:

```bash
cd garimpo_afiliado
```

Instale as dependências utilizando o CLI do CrewAI:

```bash
crewai install
```

Ou utilizando o gerenciador de pacotes de sua preferência:

```bash
# Com uv
uv sync

# Ou com pip
pip install -e .
```

## Como Executar

Execute o projeto através do comando:

```bash
crewai run
```

Ou executando o script principal via Python:

```bash
python -m garimpo_afiliado.main
```

Durante a execução, informe os dados solicitados no terminal:

1. **Plataforma**: Escolha entre `shopee`, `amazon` ou `mercado livre`.
2. **Categoria**: Informe a categoria desejada (por exemplo, `casa` ou `beleza`) ou pressione `Enter` para buscar no catálogo geral.

Ao final do processo, os relatórios são gravados na pasta `resultados/`:
- `resultados/<plataforma>_<data_hora>.json`: Saída estruturada de todas as tarefas.
- `resultados/<plataforma>_<data_hora>.md`: Relatório textual consolidado.
