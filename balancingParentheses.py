def balanco(expressao):
    pilha = []

    for caracter in expressao:
        if caracter == '(':
            pilha.append(caracter)
        elif caracter == ')':
            if not pilha:
                return False
            pilha.pop()

    return len(pilha) == 0

while True:
    expressao = input("Digite uma expressão com parênteses ou 'q' para sair: ")
    
    if expressao.lower() == 'q':
        break

    if balanco(expressao):
        print("Os parênteses estão balanceados.")
    else:
        print("Os parênteses estão desbalanceados.")
