def obter_numero_inteiro():
    try:
        numero = int(input("Digite um número inteiro: "))
        return numero
    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido.")
        return None

def main():
    numero = obter_numero_inteiro()
    if numero is not None:
        print(f"Você digitou o número: {numero}")

if __name__ == "__main__":
    main()