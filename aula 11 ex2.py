def comparar_par_impar(num1, num2):
    """
    Compara se dois números são pares ou ímpares
    Retorna uma string com o resultado da comparação
    """
    resultado_num1 = "par" if num1 % 2 == 0 else "ímpar"
    resultado_num2 = "par" if num2 % 2 == 0 else "ímpar"
    
    return f"O primeiro número ({num1}) é {resultado_num1} e o segundo número ({num2}) é {resultado_num2}"

print(comparar_par_impar(2, 3))  
print(comparar_par_impar(7, 6))  
print(comparar_par_impar(9, 12)) 