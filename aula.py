#pessoa_1

pessoa1_nome = nome = input('Nome')
pessoa1_idade = idade = input('Idade')


#pessoa_3

pessoa3_nome = nome = input('Nome')
pessoa3_idade = idade = input('Idade')

"quartos"
["simples" , "duplo" , "luxo"]


"precos"
["100,00" , "150,00" , "250,00"]


pessoa1_quarto = input("escolha o tipo de quarto " + pessoa1_nome + " (simples , duplo ou luxo): ") 

pessoa3_quarto = input ("escolha o tipo de quarto" + pessoa3_nome + " (simples , duplo ou luxo): ")



#dias = 
pessoa1_dias = int(input("quantos dias " + pessoa1_nome + "vai ficar no hotel? "))

pessoa3_dias = int(input("quantos dias " + pessoa3_nome + "vai ficar no hotel? "))

#calculos = 
if pessoa1_quarto == "simples" : 
    pessoa1_total = 100 * pessoa1_dias
    print(pessoa1_total)
elif pessoa1_quarto == "duplo" : 
    pessoa1_total = 150 * pessoa1_dias
    print(pessoa1_total)
elif pessoa1_quarto == "luxo" : 
    pessoa1_total = 250 * pessoa1_dias
    print (pessoa1_total)

    print("\n--- pagamento ---")
    print(f"{pessoa1_nome} irá pagar: R${pessoa1_total}")


    if pessoa3_quarto == "simples" : 
     pessoa3_total = 100 * pessoa3_dias
     print(pessoa3_total)
elif pessoa3_quarto == "duplo" : 
    pessoa3_total = 150 * pessoa3_dias
    print(pessoa3_total)
elif pessoa3_quarto == "luxo" : 
    pessoa3_total = 250 * pessoa3_dias
    print (pessoa3_total)

    print("\n--- pagamento ---")
    print(f"{pessoa3_nome} irá pagar: R${pessoa3_total}")