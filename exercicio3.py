def primo(numero):
    
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeroinserido = int(input("Digite um número inteiro positivo maior que 1: "))


if primo(numeroinserido):
    print(f"O número {numeroinserido} é primo.")
else:
    print(f"O número {numeroinserido} não é primo.")
