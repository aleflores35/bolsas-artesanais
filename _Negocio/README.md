# Área de Negócio

Esta pasta separa as decisões de **negócio** do código do aplicativo (que fica na raiz do projeto). São duas trilhas distintas:

## 1. `Atelie-Lisandra/`
A empresa que faz e vende bolsas artesanais. Marca, operação, finanças, fornecedores, vendas e canais. É o negócio "real" da Lisandra.

## 2. `Produto-SaaS/`
O sistema que construímos para o ateliê, tratado como **produto vendável** para outros ateliês e marcas. Posicionamento, precificação, modelo de receita e plano de lançamento.

## Por que separadas
- O ateliê é uma operação de produto físico (margem por peça, estoque, produção).
- O SaaS é um produto digital (receita recorrente, custo de servidor por cliente, escala).
- As decisões, métricas e riscos de cada uma são diferentes — misturar atrapalha.

> O ateliê pode virar a **primeira cliente / caso de sucesso** do SaaS. Essa é a ponte natural entre as duas trilhas.

_Esta pasta fica fora do controle de versão (git) do aplicativo._
