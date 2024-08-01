def somar_intervalo():
 
    inicio = int(input("Digite o início do intervalo: "))
    fim = int(input("Digite o fim do intervalo: "))

    intervalo_tamanho = fim - inicio + 1

    if intervalo_tamanho > 100:
        print("O intervalo não pode ter mais de 100 números.")
        return

    soma = sum(range(inicio, fim + 1))

    print(f"A soma dos números no intervalo de {inicio} a {fim} é {soma}.")

somar_intervalo()
