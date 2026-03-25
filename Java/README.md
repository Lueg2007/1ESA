<h1 align="center">Repositório de Aulas e Tarefas – Java (2ESA)</h1>
<p align="center">Exercícios práticos e projetos desenvolvidos em Java para a disciplina de Engenharia de Software / DDD na FIAP</p>

<p align="center">
  <img src="https://img.shields.io/badge/Java-21+-ED8B00?logo=openjdk&logoColor=white" alt="Java 21+">
  <img src="https://img.shields.io/badge/FIAP-Engenharia%20de%20Software-E4002B" alt="FIAP">
</p>

---

### 📖 Sobre o Projeto

Este repositório documenta a progressão da aprendizagem em programação orientada a objetos com Java. Ele contém todos os códigos desenvolvidos durante as aulas (da Aula 01 à Aula 08) e as respetivas tarefas práticas de consolidação.

Os projetos evoluem desde a sintaxe básica e uso de variáveis, passando por entrada e saída de dados com interface gráfica e consola, até à modelação de classes do mundo real (Orientação a Objetos) com atributos, métodos e regras de negócio de cálculo financeiro.

---

### 📁 Estrutura do Projeto

O repositório está dividido em duas categorias principais de aprendizagem:

```text
Java/
├── Aula01/ a Aula08/     # Códigos abordados em sala de aula
│   ├── Primitivo.java    # Fundamentos e tipos de variáveis
│   ├── EntradaDeDados... # I/O com Scanner e JOptionPane
│   └── classes/          # Introdução à POO (Radio, Televisor, ArCondicionado)
│
└── Tarefas/              # Exercícios práticos e de lógica de negócio
    ├── Tarefa01/         # Cálculos matemáticos simples (Média, Idade, Área)
    ├── Tarefa02/         # Sistema de Folha de Pagamento
    └── Tarefa03/         # Sistema de Gestão de Ingressos para Eventos

```

---

### 🧮 Principais Regras de Negócio (Tarefas em Destaque)

O repositório contém várias implementações focadas na lógica de negócio. Destacam-se:

**Classe `FolhaDePagamento` (Tarefa 02)**

* `salarioBruto` e `numeroDeDependentes` — dados base do colaborador.
* `descontoINSS` e `valorPlanoDeSaude` — variáveis para cálculo de deduções.
* `calcularSalarioLiquido()` — deduz a percentagem de INSS e o custo do plano de saúde (multiplicado pelos dependentes + 1) ao salário bruto.

**Classe `Eventos` (Tarefa 03)**

* `bebida`, `comida`, `equipe`, `show` — despesas totais do evento.
* `calcularValorDoIngresso()` — soma todas as despesas, aplica a margem de `lucro` desejada e divide pelo número de `convidados` para definir o preço unitário do ingresso.

---

### ▶️ Como Executar

**Pré-requisitos:** Java 21 ou superior instalado.

Pode compilar e executar qualquer ficheiro `Main` ou classe com método principal. Abaixo está o exemplo para rodar a Tarefa 02 via Consola:

```bash
# Navegar até ao diretório do projeto desejado
cd Java/Tarefas/Tarefa02

# Compilar as classes
javac -d out src/br/fiap/com/bean/FolhaDePagamento.java src/br/fiap/com/main/MainScanner.java

# Executar a aplicação
java -cp out br.fiap.com.main.MainScanner

```

---

### 💻 Exemplo de Uso (Folha de Pagamento)

```text
Digite seu salário bruto: 
10000
Digite o número de dependentes: 
4
Digite o desconto de INSS: 
15
Digite o valor do plano de saúde: 
150

Salário Bruto: R$ 10000,00
Número de dependentes: 4
INSS: 15,0%
Plano de saúde: R$ 150,00
Salário líquido: R$ 7750,00

```

---

### 🚀 Tecnologias Utilizadas

| Tecnologia | Uso |
| --- | --- |
| **Java 21+** | Linguagem principal para construção da lógica e POO |
| **java.util.Scanner** | Leitura de dados via consola |
| **javax.swing.JOptionPane** | Criação de caixas de diálogo para I/O visual |
| **IntelliJ IDEA** | IDE de desenvolvimento |

---

### 👥 Autor

<table>
<td align="center">
<a href="https://github.com/Lueg2007">
<img src="https://github.com/Lueg2007.png" width="100px;" alt="Lueg2007"/>
<br />
<sub><b>Luigi Escudero Grigoletto</b></sub>
</a>
<br />
<sub>RM 562505</sub>
</td>
</tr>
</table>
