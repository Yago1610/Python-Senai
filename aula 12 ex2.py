def divisao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida!")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

def nome():
    print("Programa de Divisão de Números")

# Chamando as funções
nome()
divisao()