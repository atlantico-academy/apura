# Detecção de notícias falsas veiculadas em português

Neste projeto almejamos desenvolver um modelo capaz de indicar a confiabilidade de trechos de notícias relacionadas aos presidenciáveis. Para tanto, utilizaremos técnicas de aprendizado de máquina e dados de notícias falsas e autênticas. O modelo produzido deverá alcançar acurácia maior que 80% nos testes finais e deverá ser disponibilizado em plataforma web que poderá ser utilizada por leigos.

Os dados já [disponíveis](https://github.com/roneysco/Fake.br-Corpus) estão etiquetados entre notícias falsas e verdadeiras e este escopo deverá ser aumentado através de web scraping em portais de agências de checagem de notícias, o que facilitará a etiquetagem dos dados obtidos. Os recursos computacionais para a análise exploratória dos dados, construção dos modelos e de implementação da solução advém dos computadores pessoais dos próprios desenvolvedores da equipe. 

Os requerimentos para completude do projeto envolvem: aquisição de mais dados de notícias com diferentes etiquetas, definição das funções de limpeza, pré-processamento e codificação dos dados, padronização dos vocábulos utilizados nos textos, extração dos vetores dos textos, construção e comparação de modelos de aprendizado de máquina, obtenção e seleção de modelo com acurácia superior a 80% e implementação do modelo em página web acessível ao usuário final.

Riscos: falha em atingir o nível de acurácia estabelecido como meta para o projeto, dados usados não estarem totalmente certos, banco de dados ser insuficiente para algumas análises. Contingências (ainda por definir).

Metas de mineração: Realizar web scraping pelo menos uma vez ao dia com o objetivo de buscar o máximo de notícias. O objetivo será concluído se houver a coleta de mais de uma notícia de cada objeto de estudo.

Este projeto será desenvolvido utilizando a linguagem python (versão 3.8.10), devido a sua facilidade para manipular dados e as operações com dados existentes das bibliotecas.

Em relação às bibliotecas, para cada etapa serão utilizadas, respectivamente:
- Web scraping
     - Beautiful soup
     - Selenium
- Limpeza de dados
     - NLTK
- Análise Exploratória dos Dados:
     - Pandas
     - Numpy
     - Seaborn
     - Matplotlib.lib
     - Path
- Criação do pipeline, treinamento e validação dos modelos:
     - Scikit-learn
     - SHAP
- Modelo em Produção
     - Heroku Cloud

## Objetivos e resultados chave

Em termos simples, os "Objetivos" se relacionam com a meta do projeto, e os "Resultados-Chave" expressam como essa meta será alcançada. Os Objetivos e resultados chave devem ser definidos no início de um projeto. A ideia é escolher uma métrica associada a um projeto e defini-la como o objetivo. Isso mostra a meta que você deseja alcançar. Em seguida, os resultados-chave são definidos para mostrar como atingir o objetivo. Os resultados principais são mensuráveis ​​e geralmente limitados a três a cinco por objetivo.

Em síntese, os objetivos estão ligados as entregas e os resultados chave aos passos que precisam se seguir para conseguir alcançar os resultados.
Exemplo de objetivos e resultados chave aplicados a projetos de ciência de dados.



 - Realizar uma análise exploratória de dados [Fake.br-Corpus de @roneysco](https://github.com/roneysco/Fake.br-Corpus)
    - Identificar variáveis, descrevê-las e definir os tipos de dados
    - Remover palavras irrelevantes, emojis, etc
    - Lematizar as palavras flexionadas
 - Adquirir novas informações falsas e verdadeiras
    - Realizar webscraping de portais com notícias já etiquetadas
    - Higienizar os dados coletados
    - Disponibilizar na forma de corpus
 - Criar modelo de detecção de informações falsas
    - Transformar os textos em vetores
    - ...
 - ...

## Conteúdo

Utilize esta seção para descrever o que cada notebook faz. Se tiver gerado algum relatório, também utilize essa seção para descrevêlo. Isso facilitará a leitura.

## Utilização

Descreva aqui quais os passos necessários (dependências externas, comandos, etc.) para replicar o seu projeto. Instalação de dependências necessárias, criação de ambientes virtuais, etc. Este modelo é baseado em um projeto utilizando o [Poetry](https://python-poetry.org/) como gerenciador de dependências e ambientes virtuais. Você pode utilizar o `conda`, ambientes virtuais genéricos do Python ou até mesmo containers do docker. Mas tente fazer algo que seja facilmente reprodutível.

## Desenvolvedores
 - [Tayná Fiúza](https://github.com/fiuzatayna)
 - [Contribuidor 2](http://github.com/contribuidor_2)

## Organização de diretórios

> **Nota**: essa seção é somente para entendimento do usuário do template. Por favor removê-la quando for atualizar este `README.md`

```
.
├── data/                   # Diretório contendo todos os arquivos de dados (Geralmente está no git ignore ou git LFS)
│   ├── external/           # Arquivos de dados de fontes externas
│   ├── processed/          # Arquivos de dados processados
│   └── raw/                # Arquivos de dados originais, imutáveis
├── docs/                   # Documentação gerada através de bibliotecas como Sphinx
├── models/                 # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/              # Diretório contendo todos os notebooks utilizados nos passos
├── references/             # Dicionários de dados, manuais e todo o material exploratório
├── reports/                # Análioses geradas como html, latex, etc
│   └── figures/            # Imagens utilizadas nas análises
├── src/                    # Código fonte utilizado nesse projeto
│   ├── data/               # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/         # Classes e funções utilizadas para implantação do modelo
│   └── model/              # Classes e funções utilizadas para modelagem
├── pyproject.toml          # Arquivo de dependências para reprodução do projeto
├── poetry.lock             # Arquivo com subdependências do projeto principal
├── README.md               # Informações gerais do projeto
└── tasks.py                # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
