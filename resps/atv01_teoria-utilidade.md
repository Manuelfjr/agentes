# Atividade: Teoria da Utilidade

## Grupo

* Manuel Ferreira Junior
* Wanusa Pontes

# Questão 01: Teoria da Utilidade I

## 1) Desenhe uma árvore de decisão para esse problema. Mostre as probabilidades eresultados possíveis.

**R.:**

```plaintext
                        |--> Fracasso: quebra agora (prob=0.4)
          | Reparar ----|
          |             |--> Sucesso: +1 ano de vida útil (prob=0.6)
Decisão --|
          |
          |--> Não reparar --> Quebra em 3 meses (prob=1)
```


## 2) Seja U(x) a função de utilidade do equipamento,onde x é o número de meses devida útil remanescente. Assumindo que U(12)=1.0 e U(0)=0, qual a mínima utilidade da vida útil de 3 meses, para o reparo não ser indicado.

**R.:** Calculado a utilidade esperada do reparo, então:

para o sucesso do reparo, temos U(12) = 1.0 e P(U(12)) = 0.6 como a vida útil restante, considerando 12 meses e U(0) = 0, referente a quebra do equipamento pos o reparo e P(U(0)) = 0.4. Então aplicando na formula, temos:

<p align="center">
EU = 0.6 &middot; U(12) + 0.4 &middot; U(0) &rarr; <br>
EU = 0.6 &middot; 1 + 0.4 &middot; 0 &rarr;
<br>
EU = 0.6
</p>

logo, temos as seguintes decisões:

* **1)** se: U(3) > 0.6, logo não reparar tem mais utilidade;

* **2)** se: U(3) < 0.6, logo reparar tem mais utilidade.

então, a mínima utilidade da vida útil de 3 meses é de 0.6 (U(3) > 0.6), logo o reparo não é indicado ser feito em apenas 3 meses.

## 3) Pedro descobriu que existe um teste menos arriscado que fornece a chance do              equipamento não ser danificado durante o reparo.Quando o resultado do teste é positivo,a probabilidade do equipamento ser bem reparado aumenta. O teste tem as seguintes características:

* **A probabilidade do resultado do teste ser positivo quando o equipamento não quebra é 0.9.**
 
* **A probabilidade do resultado do teste ser positivo quando o equipamento quebra é 0.2.**
 
Qual a probabilidade do equipamento "sobreviver" ao reparo dado que o teste é positivo?
---

**R.:**
```plaintext
                                     |
                    |----------------|----------------|
                    |                                 |
Reparo:             S (P = 0.6)                       F (P = 0.4)
                    |                                 |
            |-------|-------|                 |-------|-------|
            |               |                 |               |
T:          + (0.9)         - (0.1)           + (0.2)         - (0.8)
```

Logo, note que:

1) P(S) = 0.6

2) P(F) = 0.4

3) P(T<sup>+</sup> | S) = 0.9

4) P(T<sup>-</sup> | S) = 1 - P(T<sup>+</sup> | S) = 1 - 0.9 = 0.1

5) P(T<sup>+</sup> | F) = 0.2

6) P(T<sup>-</sup> | F) = 1 - P(T<sup>+</sup> | F) = 1 - 0.2 = 0.8


O nosso objetivo é calcular P(S | T<sup>+</sup>), dado por:

<p align="center">
P(S | T<sup>+</sup>) = [P(S &#x2229; T<sup>+</sup>)]/P(T<sup>+</sup>) = [P(S) &middot; P(T<sup>+</sup> | S)] / P(T<sup>+</sup>)
</p>


Vamos calcular P(T<sup>+</sup>) utilizando o teorema da probabilidade total, temos:


<p align="center">
P(T<sup>+</sup>) = P(T<sup>+</sup> | S) &middot; P(S) + P(T<sup>+</sup> | F) &middot; P(F) = <br>
= 0.9 &middot; 0.6 + 0.2 &middot; 0.4 = <br>
= 0.62
</p>

<p>
&#x2234; P(T<sup>+</sup>) = 0.62
</p>

Logo, substituindo os devidos valores na fórmula anterior, temos:

<p align="center">
P(S | T<sup>+</sup>) = [P(S) &middot; P(T<sup>+</sup> | S)] / P(T<sup>+</sup>) = <br>
= [0.6 &middot; 0.9] / 0.62 &asymp; 0.87
</p>

&#x2234; P(S | T<sup>+</sup>) = 0.87

Então, a probabilidade do equipamento sobreviver ao reparo dado que o teste é positivo é de 0.87.

## 4)  Assumindo que o teste no equipamento foi feito, sem custo, e o resultado foi positivo, Pedro deve realizar o reparo? Assuma que U(3) = 0.7.

**R.:** Dado os valores abaixo:

1) P(S | T<sup>+</sup>) = 0.87 ;

2) U(3) = 0.7

Logo:

<p align="center">
     P(S | T<sup>+</sup>) > U(3)  &rarr; <br>
     0.87 > 0.7
</p>
Como P(S | T<sup>+</sup>) > 0.7, então o individuo deve realizar o reparo.


## 5) Acontece que o teste em si também tem seus problemas. O equipamento também pode quebrar durante o teste. Defina a árvore de decisão para mostrando todas as decisões e consequências.

* **R.:**
```plaintext
                 |--> Quebra durante o teste
        | Testar-|
        |        |--> Teste é concluido
        |             |
        |             |--> Teste (+) |--> Reparo bem sucessido
        |             |              |
        |             |              |--> Reparo mal sucessido
        |             |
        |             |--> Teste (-) |--> Reparo bem sucessido
        |                            |
        |                            |--> Reparo mal sucessido
      --|
        | Não testar ---|--> Inutilizado em 3 meses 
```

## 6) 6. Suponha que a probabilidade do equipamento quebrar durante o teste é 0.1. Pedro deveria indicar a realização do teste? 

* **R.:**

Vamos primeiro definir os cenários, sendo eles:

* **Pedro realiza o teste:**
  * **Quebra durante o teste**: U(0) = 0 sendo P(Durante o teste) = 0.1
  * **Teste concluido com sucesso**: P(Sem quebrar no teste) = 0.9

Agora, supondo o teste concluído, sabemos que P(T<sup>+</sup>) = 0.62, então, dado "S" para sucesso, temos:

<p align="center">
  P(S | T<sup>+</sup>) = 0.87
</p>

Como visto no item 4. Além disso, temos:

<p align="center">
  U(12) = 1
</p>

Agora, se o teste é negativo, logo também como no item 4, temos P(T<sup>-</sup>) = 1 - 0.62 = 0.38. Logo, se Pedro não repara o equipamento, obtem-se uma utilidade de 0.7 (U(3) = 0.7).

Dado isso, a utilidade do teste pode ser caclulada pela expressão abaixo:


Seja Q = "Quebra no teste" e C = "Sucesso no teste", então

<p align="center">
  EU(Teste) = P(Q) &times; U(0) + P(C) &times; [EU(C)]
</p>

Onde:

<p align="center">
  EU(C) = P(T<sup>+</sup>) &times; ( P(S | T<sup>+</sup>)&times;U(12) + (1 - P(S | T<sup>+</sup>))&times;U(0) ) + P(T<sup>-</sup>)&times;U(3)
</p>

Logo, substituindo, temos:


<p align="center">
  EU(Teste) = P(Q) &times; U(0) + P(C) &times; [P(T<sup>+</sup>) &times; ( P(S | T<sup>+</sup>)&times;U(12) + (1 - P(S | T<sup>+</sup>))&times;U(0) ) + P(T<sup>-</sup>)&times;U(3)]
</p>

Agora atribuindo os devidos valores, temos:


<p align="center">
  EU(Teste) = 0.1 &times; 0 + 0.9 &times; [0.62 &times; ( 0.87 &times; 1 + (1 - 0.87) &times; 0 ) + (1 - 0.62) &times; 0.7] =
  <br>
  = 0 + 0.9 &times; [0.62 &times; (0.87 &times; 1 + (0.13) &times; 0) + (0.38) &times; 0.7] = 
  <br>
  = 0.9 &times; [(0.62 &times; 0.87) + (0.38 &times; 0.7)] = 
  <br>
  = 0.9 &times; (0.54 + 0.27) = 
  <br>
  = 0.9 &times; 0.81 &approx; 0.73
</p>

Logo, EU(Teste) = 0.73. Então, para pedro indicar a realização do teste EU(Teste) > EU(Teste<sup>c</sup>), que de fato, 0.73 > 0.7, portanto o Pedro deve indicar a realização do teste.

-------------

# Questão 02: Teoria da Utilidade II



## 1) Desenha a árvore de decisão para suas apostas. Qual a aposta ótima e utilidades esperadas? Assuma que você é neutro a risco.

```plaintext
|-- Não apostar
|   |-- U(Não apostar) = 0
|
|-- Apostar em Bob (Custo: R$ -1)
|   |-- Bob ganha (P(B) = 0.7)
|   |   |-- Ganho: R$ 1 (U(Ganho bob) = 1)
|   |
|   |-- Bob perde (1 - P(B) = 0.3)
|       |-- Perda: R$ -1 (U(Perda bob) = 1)
|
|-- Apostar em Joe (Custo: R$ -1)
    |-- Joe ganha (P(J) = 0.1)
    |   |-- Ganho R$ 10 (U(Ganho joe) = 10)
    |
    |-- Joe perde (1 - P(J) = 0.9)
        |-- Perda: R$ -1(U(Perda joe) = 1)
```


Nesse cenário, temos duas possibildiades gerais de utilidade, Utilidade para Bob e Joe. Vamos calcular para ambos da seguinte forma:

1) U(Apostar em Bob) = P(B) &middot; 1 + P(B<sup>c</sup>) &middot; (-1) = 0.7 &middot; 1 + 0.3 &middot; (-1) = 0.7 - 0.3 = 0.4

2) U(Apostar em Joe) = P(J) &middot; 10 + P(J<sup>c</sup>) &middot; (-1) = 0.1 &middot; 10 + 0.9 &middot; (-1) = 1 - 0.9 = 0.1

Logo, as utilidades esperadas podem ser vistas abaixo.

<table align="center">
  <tr>
    <th>Opção</th>
    <th>Utilidade Esperada</th>
  </tr>
  <tr>
    <td><strong>Apostar em Bob</strong></td>
    <td><strong>0.4</strong></td>
  </tr>
  <tr>
    <td>Apostar em Joe</td>
    <td>0.1</td>
  </tr>
  <tr>
    <td>Não apostar</td>
    <td>0</td>
  </tr>
</table>

&#x2234; então a aposta ótima é Apostar em Bob, uma vez que ele apresentou a maior utilidade (U(Apostar em Bob) > U(Apostar em Joe) > U(Não apostar)).


## 2) Alguém ofereceu um desafio: ele paga 2 R$ antecipados e você paga 50% do seu lucro em qualquer aposta (i.e., 0.50 R$ se Bob ganhar e 5 R$ se Joe ganhar). Desenhe a árvore de decisão, calcule as utilidades e decisões ótimas.

* **R.:**

```plaintext
|-- Não apostar
|   |-- Utilidade: R$ 2  (antecipados)
|
|-- Apostar em Bob (Custo: R$ -1)
|   |-- Bob ganha (P(B) = 0.7)
|   |   |-- Ganho:
|   |           |lucro: R$ (1 - 0.5) = R$ 0.5
|   |           |antecipado: R$ 2.00
|   |           |total: R$ 2.50
|   |
|   |-- Bob perde (1 - P(B) = 0.3)
|       |-- Perda:
|               |lucro: R$ (0 - 1) = R$ -1
|               |antecipado: R$ 2.00
|               |total: R$ 1.00
|
|-- Apostar em Joe (Custo: R$ -1)
    |-- Joe ganha (P(J) = 0.1)
    |   |-- Ganho:
    |           |lucro: R$ (10 - 5) = R$ 5.00
    |           |antecipado: R$ 2.00
    |           |total: R$ 7.00
    |
    |-- Joe perde (1 - P(J) = 0.8)
        |-- Perda:
                |lucro: R$ (0 - 1) = R$ -1
                |antecipado: R$ 2.00
                |total: R$ 1.00
```

Vamos obter as utilidades esperadas, da seguinte forma:

1) U(Não apostar) = 2.00

2) U(Apostar em Bob) = P(B) &middot; U(B) + P(B<sup>c</sup>) &middot; (B<sup>c</sup>) = 0.7 &middot; 2.5 + 0.3 &middot; 1 = 1.75 + 0.3 = 2.05  <br>

&#x2234; U(Apostar em Bob) = 2.05

3) U(Apostar em Joe) = P(J) &middot; U(J) + P(J<sup>c</sup>) &middot; (J<sup>c</sup>) = 0.1 &middot; 7.0 + 0.9 &middot; 1 = 0.7 + 0.9 = 1.6  <br>

&#x2234; U(Apostar em Joe) = 1.06


Então, a tabela com as utilidades esperadas esta abaixo.

<br>

<table align="center">
  <tr>
    <th>Opção</th>
    <th>Utilidade Esperada</th>
  </tr>
  <tr>
    <td><strong>Apostar em Bob</strong></td>
    <td><strong>2.05</strong></td>
  </tr>
  <tr>
    <td>Não apostar</td>
    <td>2.0</td>
  </tr>
  <tr>
    <td>Apostar em Joe</td>
    <td>1.06</td>
  </tr>
</table>

Logo, supondo que sou neutro a risco,  a aposta ótima seria apostar no Bob, pois U(Apostar em Bob) > U(Não apostar) > U(Apostar em Joe).
