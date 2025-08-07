# Variáveis globais
num1 = 5
num2 = 6
num3 = 2

def multiplicar_globais():
    """Multiplica três números definidos como variáveis globais"""
    global num1, num2, num3 
    return num1 * num2 * num3

print(multiplicar_globais())  