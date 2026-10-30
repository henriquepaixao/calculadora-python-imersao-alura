# =====================================================================
# CALCULADORA EM PYTHON - QUATRO OPERAÇÕES BÁSICAS
# Projeto desenvolvido para a Imersão Alura
# =====================================================================

def adicionar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração do primeiro número pelo segundo."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto da multiplicação de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna a divisão de 'a' por 'b'.
    Lança ValueError se 'b' for igual a 0.
    """
    if b == 0:
        raise ValueError("Erro Matemático: Não é possível dividir por zero!")
    return a / b


def porcentagem(a: float, b: float) -> float:
    """
    Calcula 'b'% de um valor base 'a'.
    Exemplo: porcentagem(200, 15) retorna 30.0 (15% de 200).
    """
    return (a * b) / 100


def exibir_menu() -> None:
    """Exibe o menu de opções para o usuário."""
    print("\n" + "=" * 40)
    print("      CALCULADORA BÁSICA EM PYTHON      ")
    print("=" * 40)
    print("  [1] Adição (+)")
    print("  [2] Subtração (-)")
    print("  [3] Multiplicação (*)")
    print("  [4] Divisão (/)")
    print("  [5] Porcentagem (%)")
    print("  [0] Sair do Programa")
    print("=" * 40)


def obter_numero(mensagem: str) -> float:
    """Lê um número float do usuário com tratamento de entradas inválidas."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Entrada inválida! Digite um número real (ex: 10 ou 3.5).")


def main() -> None:
    """Função principal que orquestra o fluxo de execução."""
    print("⚡ Calculadora Python iniciada com sucesso!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0 a 5): ").strip()

        if opcao == "0":
            print("\nEncerrando a calculadora. Até logo! 👋")
            break

        if opcao not in ["1", "2", "3", "4", "5"]:
            print("\n❌ Opção inválida! Escolha um número entre 0 e 5.")
            continue

        print("\n--- Insira os Valores ---")
        if opcao == "5":
            num1 = obter_numero("Digite o valor base: ")
            num2 = obter_numero("Digite a porcentagem (%): ")
        else:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = adicionar(num1, num2)
                simbolo = "+"
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                simbolo = "-"
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                simbolo = "*"
            elif opcao == "4":
                resultado = dividir(num1, num2)
                simbolo = "/"
            elif opcao == "5":
                resultado = porcentagem(num1, num2)
                simbolo = "%"

            print("\n" + "-" * 32)
            if opcao == "5":
                print(f"✅ Resultado: {num2}% de {num1} = {resultado}")
            else:
                print(f"✅ Resultado: {num1} {simbolo} {num2} = {resultado}")
            print("-" * 32)

        except ValueError as erro:
            print(f"\n❌ {erro}")


if __name__ == "__main__":
    main()
