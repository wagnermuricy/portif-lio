-<h1 align="center">olá 👋, eu sou o Wagner</h1>
<h3 align="center">Apaixonado por ciência de dados e análise de dados</h3>

# "Seja bem vindo ao meu Portifólio"

Neste repositório, você encontrará meus projetos pessoai que venho desenvolvendo aprimorando minhas habilidades em: Python, SQL e dashboards do Power BI.

- 🌱 Atualmente estou aprendendo **Python, SQL e Power BI**
  
- 📫 Você me acha através do e-mail **wagnermuricy16@gmail.com**
  
- 📄 Estou em busca da minha primeira oportunidade na área de dados [https://www.linkedin.com/in/wagner-de-jesus-muricy]
  



## Sistema bancário

### 🔧 Ferramentas

-Python

### Descrição do projeto

Aqui está um sistema bancário com as operações: sacar, depositar e visualizar extrato.

"Operação de saque"
O sistema permite realizar 3 saques diários com limite de no máximo r$500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema irá exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.

"Operação depósito"
Deve ser possível depositar valores positivos para a conta bancaria. E todos os depósitos será armazenados em uma variável e exibidos na operação extrato.

"Operação extrato"
Essa operação irá listar todos os depósitos e saques realizados na conta. E no fim da listagem irá ser exibido o saldo atual da conta.

### Link do sistema:https://github.com/wagnermuricy/portif-lio/blob/main/sistema%20b%C3%A1ncario.py

## Automação com Python

### 🔧 Ferramentas
-Python 

-Pandas

-Pyautogui

### Descrição do projeto

Esse um projeto de automação o desafio do projeto era cadastrar 264 itens com as seguintes informações: código, marca, tipo, categoria, preço, custo e observações.
Para isso, utilizei uma base de dados, a biblioteca Pandas e a biblioteca Pyautogui.
E esse foi o resultado alcançado.

"obs.: pra você usar terá que achar as posiçoes do mouse de acordo com o seu pc"

### Link do sistema:https://github.com/wagnermuricy/portif-lio/blob/main/automa%C3%A7%C3%A3o.py

## Relatório Financeiro

![GravaodeTela2025-02-12021219-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/3bebe297-755a-4416-829d-a5df903c2af6)


### 🔧 Ferramentas
Excel

Power BI

### 📝 Competências Utilizadas
Limpeza de Dados

Tratamento de Dados

Coleta de Informações

Transformação das Informações em Insights

Visualização de Dados

### 🔗 Etapas

### 🔗 Extração
Os dados foram extraídos diretamente do Power BI.

### 🔗 Transformação / Limpeza
Nas planilhas do Excel, foram realizadas exclusões de linhas e colunas em branco para garantir a integridade dos dados.

### 🔗 Análise
Iniciei o processo de análise exploratória para obter uma visão geral dos dados, verificando a presença de dados faltantes ou duplicados, a distribuição e os tipos de dados.

Depois dessa análise inicial, criei medidas DAX para auxiliar na construção das visualizações. As medidas foram:

### DAX
Transações PIX = CALCULATE(COUNTROWS('movimentações'), 'movimentações'[Forma Pagamento] = "Pix")

Transações = COUNTROWS('movimentações')

Receita = CALCULATE(SUM('movimentações'[Valor da Movimentação]), 'movimentações'[Tipo] = "recebimento")

Imposto = [Receita] * 0.15 

Despesas = -CALCULATE(SUM('movimentações'[Valor da Movimentação]), 'movimentações'[Tipo] = "Pagamento") 

Lucro = [Receita] - [Despesas] - 'movimentações'[Imposto]

margem = [Lucro] / [Receita]

Margem Auxiliar = 1 - 'movimentações'[margem]

Desvio Margem = 'movimentações'[margem] - 0.3

1 % Pix = 'movimentações'[Transações PIX] / [Transações]


🔗 Construção das Visualizações
Após criar as medidas, construí os seguintes gráficos:

Scroller: Criado para exibir informações em tempo real.

Enlighten Data Story: Adicionado para mostrar a porcentagem das movimentações com um texto explicativo.

Além disso, quatro cartões foram criados para exibir as principais métricas:

Receita: Total de dinheiro gerado pelas operações da empresa. Um aumento ou diminuição significativa na receita pode indicar tendências de mercado ou a eficácia das estratégias de vendas.

Despesas: Reflete os custos incorridos pela empresa para gerar a receita. Identificar áreas onde os custos estão aumentando pode ajudar na tomada de decisões sobre redução de gastos.

Imposto: Mostra a carga tributária da empresa. Pode ser útil para entender como os impostos afetam a lucratividade e para planejar estratégias fiscais.

Lucro: Resultado final após deduzir todas as despesas, incluindo impostos, da receita. Um dos indicadores mais importantes, pois mostra a saúde financeira da empresa.

### 🔗 Principais Insights
Gráfico de Rosca: Criado para mostrar a margem de lucro.

Gráfico de Cascata: Criado para mostrar o lucro mensal.

Cartão de Lucro: Destaca o lucro final, essencial para entender a saúde financeira da empresa.

### 🔗 Resultados das Análises
Finalizamos a construção de um dashboard financeiro bancário, que permite um acompanhamento detalhado das movimentações tanto mensais quanto anuais dos principais bancos: Nu Bank, Safra, Santander, Bradesco e Itaú. Com esse dashboard, é possível verificar:

Receita: Total de dinheiro gerado pelas operações de cada banco.

Despesas: Custos incorridos pelas instituições financeiras.

Imposto: Carga tributária sobre a receita.

Lucro: Resultado final após deduzir todas as despesas, incluindo impostos, da receita.

O dashboard fornece uma visão abrangente e clara da saúde financeira e eficiência operacional dos bancos, facilitando a análise e tomada de decisões estratégicas.

### 🔗 Teste as funções online:https://app.powerbi.com/view?r=eyJrIjoiOGUzMmU2MjgtZDJhZC00NWQ3LWE0ZWUtMTdmMjY4NTBhN2Q1IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9



## Relatório criativo


![GravaodeTela2025-01-21000806-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/65ada28b-474d-4890-b635-2c62de2d339f)


### 🔧 Ferramentas

-Excel

-Power BI

### 📝 Skills utilizadas
- Limpeza de dados

- Tratamento de dados

- Coleta de informações

- transformação das informações em insights

- Data visualization

## 🔗 Etapas

### 🔗 Extração

Arquivo retirado do próprio Power Bi.

### 🔗 Transformação / Limpeza

Nessas planilhas do Excel as mudanças que foram preciso fazer foi excluir algumas linhas e colunas em branco.

### 🔗 Análise
Iniciei com o processo de análise exploratória, buscando uma visão geral dos dados, verificando dados faltantes ou duplicados, distribuição e tipos.

Após isso, iniciei algumas análises começando pela divisão de acordo com os dados obtidos e dividi esse relatório em duas páginas.

Página 1

Na primeira página, após algumas análises, decidi organizar todas as informações relacionadas às vendas. Desta forma, é possível acompanhar todas as vendas, a quantidade de produtos vendidos, o segmento desses produtos e os países de destino. Além disso, essas análises podem ser visualizadas de forma diária, mensal e anual.

obs: Nos cartes sales x segmento e no sales x country foi adicionado 2 botões em cada um assim podendo mudar os gráficos.

Página 2

Na segunda página, seguindo as análises, foi adicionado o lucro detalhado, separado por produto, país, data e classe.


### 🔗 Resultados das análises

Com as análises realizadas, eu aprendi a organizar e detalhar informações de vendas e lucros, facilitando o acompanhamento e a obtenção de insights valiosos sobre o desempenho de produtos, países, datas e classes.assim podendo fazer o acompanhamento anual dessa empresa para assim tomar decisôes futuras.

E no relatório tamben aprendi a colocar botões flutuantes tanto para mudar o gráfico quanto para mudar de página.

### 🔗 Teste as funções online:https://app.powerbi.com/view?r=eyJrIjoiZjU2NzQ2MzgtZmZiNy00MjRmLWIxOTAtMzNiM2NlNGEzN2YyIiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9



## Dashboard de vendas

![Dashboarddevendas-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/5cfe0fd9-2eaf-4925-9547-07f04ef05cfb)

### 🔧 Ferramentas

-Excel

-Power BI

### 📝 Skills utilizadas
- Limpeza de dados

- Tratamento de dados

- Coleta de informações

- transformação das informações em insights

- Data visualization

## 🔗 Etapas

### 🔗 Extração

Arquivo retirado do próprio Power Bi.

### 🔗 Trasnformação / Limpeza

Nessas planilhas do Excel as mudanças que foram preciso fazer foi excluir algumas linhas e colunas em branco.

### 🔗 Análise
Iniciei com o processo de análise exploratória, buscando uma visão geral dos dados, verificando dados faltantes ou duplicados, distribuição e tipos.

Após isso, iniciei algumas análises começando pela divisão de acordo com os dados obtidos.

### 🔗 Resultados das análises

Com a análise dos dados, decidi dividir o dashboard em 3 páginas, assim deixando a visualização mais fácil.

### Página 1
Na página 1, tudo ficou relacionado às vendas dos produtos, onde é possível acompanhar os resultados obtidos mês a mês, ano a ano. Adicionei a média de venda dos produtos, assim, com os resultados, é possível acompanhar o desenvolvimento mensal e anual para fazer uma projeção futura.


### Página 2

Já nesta segunda página, decidi adicionar os lucros obtidos e suas médias, tudo separado por mês, ano e por país, facilitando acompanhar o faturamento obtido mensal e anual.


### Página 3 

Nessa página estão os gráficos mostrando a distribuição de lucros, vendas e unidades vendidas por país e segmento.

### Com isso, conseguimos observar todos os dados anuais dessa empresa, sabendo quais foram os produtos vendidos mês a mês, ano a ano, e os lucros obtidos por produto e o faturamento total, tudo separado, facilitando assim uma projeção futura.


### 🔗 Teste as funções online: https://app.powerbi.com/view?r=eyJrIjoiMzkzYWJiN2ItYzhhNi00OWZhLTgxYWYtMTM2M2M3Njk0Yzk3IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9


## Dashboard de RH

![DashboarddeRH-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/0267a9fb-a705-44f1-bcfa-162175ca2ed6)


### 🔧 Ferramentas

- Excel
  
- Power Bi

### 📝 Skills utilizadas

- Limpeza de dados

- Tratamento de dados

- Coleta de informações

- transformação das informações em insights

- Data visualization

## 🔗 Etapas

### 🔗 Extração

Esses dados foram disponibilizados pela hashtag onde eu aprendi a criar esse relatório

### 🔗 Trasnformação / Limpeza
Nessas planilhas do Excel as mudanças que foram preciso fazer foi excluir algumas linhas e colunas em branco.

### 🔗 Análise

Iniciei com o processo de análise exploratória, buscando uma visão geral dos dados, verificando dados faltantes ou duplicados, distribuição e tipos, dados em brancos.

### 🔗 Resultados das análises

Esse dashboar ficou bem interessante, após analizar os dados eu escolhi destacar os principais pontos:
Numeros de funcionários que estão ativos, os demitidos, a quantidade de contratações, separei funcionários por gênero, por cidade e por cargo.

Por último adicionei um TOOLTIP  para facilitar a visualização.

### Com o resultado ficará bem mais fácil de saber onde está cada funcionário e seus devidos cargos,a quantidade por gênero, observar a quantidade de demissões em caso de projeção podendo almentar ou diminuir o quadro.


### 🔗 Teste as funções online: https://app.powerbi.com/view?r=eyJrIjoiNjU5OGIzYTYtNzJjZi00NTU5LTgzMTctOWE4MGE1OTZiNTI3IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9


## analise_dataset_kaggle_diabetes

![Analise_dataset_kaggle-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/db52a7b7-1164-419b-a2dd-328cb37e889e)

### 🔧 Ferramentas
- Excel
  
- Power BI

### 📝 Skills utilizadas
- Limpeza de dados

- Tratamento de dados

- Coleta de informações

- transformação das informações em insights

## 🔗 Etapas

### 🔗 Extração
Essa tabela do excel é pública e foi retirada do site kaggle

### 🔗 Trasnformação / Limpeza

Esses dados ja estavam bem limpos então só precisei excluir colunas duplicadas.

### 🔗 Análise
Iniciei com o processo de análise exploratória, buscando uma visão geral dos dados, verificando dados faltantes ou duplicados, distribuição e tipos, dados em brancos.


### 🔗 Resultados das análises
Nesse dashboard eu utilizei uma base de dados relacionados a diabetes na população.

### conseguimos destacar a mediana de glicose e a média da diabetes relacionada a faixa etária.

### 🔗 Teste as funções online:https://app.powerbi.com/view?r=eyJrIjoiMDA5ODgzODgtOTVmYi00ZTU5LTkzMGQtNGJkZmI1ZDVhNDU0IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9

## Dashboard de produção


![Gravao-de-Tela-2024-11-25-120629-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/95943980-e28a-4560-beb4-dcd02fdd4a95)


### 🔧 Ferramentas
- Excel
  
- Power BI

### 📝 Skills utilizadas
- Limpeza de dados

- Tratamento de dados

- Coleta de informações

- transformação das informações em insights

## 🔗 Etapas

### 🔗 Extração
Essa tabela do excel é pública e foi retirada do site kaggle

### 🔗 Trasnformação / Limpeza
- Trasnformação
  Para a transformação foi preciso adicionar 7 medidas que foram:

### HORAS PRODUZIDA
HORAS PRODUZIDAS = CALCULATE(SUM('BASEPRODUÇÃO'[TOTAL HORAS]), 'BASEPRODUÇÃO'[OCORRÊNCIA]=BLANCK())

### HORAS PARADAS
HORAS PARADAS = CALCULATE(SUM('BASEPRODUÇÃO'[TOTAL HORAS]), 'BASEPRODUÇÃO'[OCORRÊNCIA]<>BLANCK())

### HORAS
HORAS = SUM('BASEPRODUÇÃO'[TOTAL HORAS])

### DISPONIBILIDADE
DISPONIBILIDADE = ([HORAS PRODUZIDAS])/(HORAS PRODUZIDAS] + [HORAS PARADAS])

### QUANTIDADE PRODUZIDA
QUANT.PRODUZIDA = SUM('BASEPRODUÇÃO'[QTDPRODUZIDA])

### QUANTIDADE REJEITADA
QUANT. REJEITADA = SUM('BASEPRODUÇÃO'[QTD REJEITADA]

### QUALIDADE
QUALIDADE = ([QUANT. PRODUZIDA])/([QUANT. PRODUZIDA] + [QUANT.REJEITADA])


### 🔗 Análise
Iniciei com o processo de análise exploratória, buscando uma visão geral dos dados, verificando dados faltantes ou duplicados, distribuição e tipos, dados em brancos.

Depois disso fui para a criação do dasboard
### 1° passo
- Foi criado
4 cartões de linha múltipla 
1 gráfico de área
2 gráficos de velocímetro 
1 cartão de segmentação de dados

### 2° passo
- adicionando imagens.
Depois dos gráficos criados entrei no site www.flaticon.com e baixei algumas imagens para adicionar nos gráficos de cartões de linha múltiplas.

### 🔗 Resultados das análises

Após finalizado foi possível destacar os seguintes insights:

1° Quantidade produzida
2° Quantidade rejeitada
3° Horas produtivas
4° Horas paradas
5° Destacar a produção de cada operador
6° A produção mensal
7° Mostra a porcentagem da disponibilidade
8° Mostra a porcentagem da qualidade.

### Com tudo, é possível acompanhar os resultados de cada funcionário, acompanhando sua projeção mensal, acompanhando o desenvolvimento de cada colaborador.

### 🔗 Teste as funções online:https://app.powerbi.com/view?r=eyJrIjoiMDAzOTA3OTctM2ZiNi00ODFiLWJiZDEtMTcwYmVjYTA3OGE5IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9















