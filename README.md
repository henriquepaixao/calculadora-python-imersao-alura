# 🐍 Calculadora em Python - Quatro Operações Básicas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/Imersão-Alura-0070f3?style=for-the-badge" alt="Imersão Alura" />
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge" alt="Status Concluído" />
  <img src="https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge" alt="Licença MIT" />
</p>

> Projeto desenvolvido durante os estudos na **Imersão da Alura**, focado na prática dos fundamentos da linguagem Python, lógica de programação, funções e tratamento de exceções.

---

## 📌 Sobre o Projeto

Este repositório contém uma **Calculadora de Terminal (CLI)** desenvolvida em Python que executa com precisão as quatro operações matemáticas fundamentais:
- ➕ **Adição** (`a + b`)
- ➖ **Subtração** (`a - b`)
- ✖️ **Multiplicação** (`a * b`)
- ➗ **Divisão** (`a / b`) com tratamento especial e seguro contra **divisão por zero**.

O projeto foi construído seguindo as convenções da **PEP 8**, boas práticas de desenvolvimento de software, funções puras e validação contínua de entradas de dados.

---

## 🚀 Funcionalidades

- [x] **Quatro operações aritméticas puras**: Funções dedicadas com *type hints* para clareza e manutenção.
- [x] **Menu Interativo no Terminal**: Interface simples e amigável via loop contínuo (`while True`).
- [x] **Tratamento de Exceções**:
  - `try...except ValueError`: Evita que o programa feche abruptamente caso o usuário digite letras ou caracteres especiais no lugar de números.
  - Validação de divisão por zero: Intercepta divisões por `0` e exibe aviso pedagógico sem quebrar a execução.
- [x] **Suporte a Números Reais (Floats)**: Aceita tanto inteiros quanto números decimais (ex: `12.5`, `-3.2`).
- [x] **Modularidade**: Funções reutilizáveis que podem ser importadas em outros scripts sem acionar o menu automaticamente (`if __name__ == "__main__":`).

---

## 💻 Demonstração de Uso no Terminal

```text
========================================
      CALCULADORA BÁSICA EM PYTHON      
========================================
  [1] Adição (+)
  [2] Subtração (-)
  [3] Multiplicação (*)
  [4] Divisão (/)
  [0] Sair do Programa
========================================
Escolha uma opção (0 a 4): 4

--- Insira os Valores ---
Digite o primeiro número: 45
Digite o segundo número: 5

--------------------------------
✅ Resultado: 45.0 / 5.0 = 9.0
--------------------------------
```

---

## 🧠 Conceitos Praticados na Imersão Alura

Durante o desenvolvimento deste projeto na Imersão da Alura, foram aplicados os seguintes conceitos:

1. **Variáveis e Tipos de Dados Primitivos**: Manipulação de strings, floats, ints e booleanos.
2. **Operadores Aritméticos**: Uso dos operadores nativos `+`, `-`, `*`, `/`.
3. **Estruturas Condicionais**: Utilização de `if`, `elif` e `else` para controle do fluxo de decisões.
4. **Estruturas de Repetição**: Loop `while` com cláusulas de escape (`break` e `continue`).
5. **Declaração de Funções**: Definição de blocos com `def`, parâmetros nomeados e retorno explícito (`return`).
6. **Docstrings e Tipagem (PEP 484)**: Documentação de funções e anotações de tipos (`a: float, b: float -> float`).
7. **Tratamento de Erros (Exceptions)**: Utilização de blocos `try` e `except` para criar código resiliente.

---

## 🛠️ Como Executar o Projeto Localmente

### Pré-requisitos
- Ter o **Python 3.8** ou superior instalado em sua máquina. Para verificar:
  ```bash
  python --version
  # ou no Linux/macOS:
  python3 --version
  ```

### Passo a Passo

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/henriquepaixao/calculadora-python-alura.git
   ```

2. **Acesse a pasta do projeto**:
   ```bash
   cd calculadora-python-alura
   ```

3. **Execute a calculadora**:
   ```bash
   python calculadora.py
   # ou
   python3 calculadora.py
   ```

---

## 📂 Estrutura de Arquivos

```
├── calculadora.py         # Script principal com as funções e menu CLI interativo
├── test_calculadora.py    # (Opcional) Testes automatizados com unittest
└── README.md              # Documentação completa do repositório
```

---

## 🧪 Rodando os Testes Unitários

Caso queira validar as funções matematicamente com testes automatizados:

```bash
python -m unittest test_calculadora.py
```

---

## 🌟 Desafios & Próximos Passos (Evolução)

- [ ] Adicionar suporte a cálculo de porcentagem (`%`) e exponenciação (`**`).
- [ ] Adicionar cálculo com múltiplos números em sequência.
- [ ] Implementar histórico em arquivo de texto (`historico.txt`).
- [ ] Criar interface gráfica com `Tkinter` ou `CustomTkinter`.

---

## 👨‍💻 Autor

Desenvolvido por **Henrique Paixão** durante a **Imersão da Alura**.

- 💼 **LinkedIn**: [linkedin.com/in/henriquepaixao](https://www.linkedin.com/in/henriquepaixao/)
- 🐙 **GitHub**: [github.com/henriquepaixao](https://github.com/henriquepaixao)

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE). Sinta-se livre para usar, estudar e aprimorar o código!
