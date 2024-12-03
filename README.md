# "Seja bem vindo ao meu Portifólio"

Neste repositório, você encontrará dois tipos de arquivos: projetos de código em Python e dashboards do Power BI.

# Python
Para acessar os projetos de Python, entre no repositório e escolha o arquivo que deseja visualizar. Obs: Se você abrir o arquivo e clicar em " ...", verá uma breve descrição do projeto.

# Dashboards
Para visualizar os dashboards, você tem duas opções:

1° Entre no repositório e veja em PDF.

2° No "README", você encontrará uma descrição dos dashboards e, abaixo de cada um, um link para acessá-los diretamente no Power BI, onde poderá testar as funções.



"Dashboard de vendas"

Nesse dashboard de vendas foi destacado as vendas, média e soma dos produtos, tudo separado e ainda é posivél verificar todos esses dados separados por mês ou por anos basta escolher.
Também é possivél verificar os todos esses dados separados por países, e olhar todos os resultados inclusives dos lucros.

link: https://app.powerbi.com/view?r=eyJrIjoiMzkzYWJiN2ItYzhhNi00OWZhLTgxYWYtMTM2M2M3Njk0Yzk3IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9

"Dashboard de RH"

Esse dashboar ficou bem interessante, após analizar os dados eu escolhi destacar os principais pontos:
Numeros de funcionários que estão ativos, os demitidos, a quantidade de contratações, separei funcionários por gênero, por cidade e por cargo.

Por último adicionei um TOOLTIP  para facilitar a visualização.

Resultado: Com o resultado ficará bem mais fácil de saber onde está cada funcionário e seus devidos cargos, em caso de projeção podendo almentar ou diminuir o quadro.

link: https://app.powerbi.com/view?r=eyJrIjoiNjU5OGIzYTYtNzJjZi00NTU5LTgzMTctOWE4MGE1OTZiNTI3IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9

"analise_dataset_kaggle_diabetes"

Esse foi o primeiro dashboard que eu fiz utilizando base de dados do site kaggle.
nesse dashboard eu utilizei uma base de dados relacionados a diabetes na população.
resultados das analises: 
conseguimos destacar a média da glicose e a média da diabetes relacionada a faixa etária.

link:https://app.powerbi.com/view?r=eyJrIjoiMDA5ODgzODgtOTVmYi00ZTU5LTkzMGQtNGJkZmI1ZDVhNDU0IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9

"Dashboard de produção"



https://github.com/user-attachments/assets/d9dc4a93-bfd7-4f68-8e33-114dc960014c



Para fazer esse dashboard foi feito os seguintes passos.

1° Importação dos dados
Após baixar os dados as únicas mudanças iniciais no processo de extração foi excluir linhas e colunas em branco.

2° Criando as medidas com fórmula DAX
Foram criado 7 medidas irei descrever cada uma.

"HORAS PRODUZIDAS"
HORAS PRODUZIDAS = CALCULATE(SUM('BASEPRODUÇÃO'[TOTAL HORAS]), 'BASEPRODUÇÃO'[OCORRÊNCIA]=BLANCK())

"HORAS PARADAS"
HORAS PARADAS = CALCULATE(SUM('BASEPRODUÇÃO'[TOTAL HORAS]), 'BASEPRODUÇÃO'[OCORRÊNCIA]<>BLANCK())

"HORAS"
HORAS = SUM('BASEPRODUÇÃO'[TOTAL HORAS])

"DISPONIBILIDADE"
DISPONIBILIDADE = ([HORAS PRODUZIDAS])/(HORAS PRODUZIDAS] + [HORAS PARADAS])

"QUANTIDADE PRODUZIDA" 
QUANT.PRODUZIDA = SUM('BASEPRODUÇÃO'[QTDPRODUZIDA])

"QUANTIDADE REJEITADA"
QUANT. REJEITADA = SUM('BASEPRODUÇÃO'[QTD REJEITADA]

"QUALIDADE"
QUALIDADE = ([QUANT. PRODUZIDA])/([QUANT. PRODUZIDA] + [QUANT.REJEITADA])

3° criação do dashboard
"Foi criado" 

4 cartões de linha múltipla 
1 gráfico de área
2 gráficos de velocímetro 
1 cartão de segmentação de dados

4° adicionando imagens.
Depois dos gráficos criados entrei no site www.flaticon.com e baixei algumas imagens para adicionar nos gráficos de cartões de linha múltiplas.

5° Resultado das analises 

Com tudo já finalizado os resultados foram destacar os seguintes pontos:

1° Quantidade produzida
2° Quantidade rejeitada
3° Horas produtivas
4° Horas paradas
5° Destacar a produção de cada operador
6° A produção mensal
7° Mostra a porcentagem da disponibilidade
8° Mostra a porcentagem da qualidade.

Link:https://app.powerbi.com/view?r=eyJrIjoiMDAzOTA3OTctM2ZiNi00ODFiLWJiZDEtMTcwYmVjYTA3OGE5IiwidCI6ImQ1NTZmMWRlLTA1ZDMtNDNiZC1iMGMyLTIzODY4ZWEyNGFlNSJ9















