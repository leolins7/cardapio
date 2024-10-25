def menu ():
    print ("1 - Café Americano - R$ 5 ")
    print ("2 - Capuccino - R$ 7 ")
    print ("3 - Café com leite - R$ 6 ")
    print ("4 - Encerrar Pedido")
valor = 0
while True: 
    menu ()
    codigo = int(input("Informe o código do seu pedido: "))
    if codigo == 0:
        print ("Código Inválido. Por favor informe um código válido.")
        continue
    elif codigo > 4:
        print ("Código Inválido. Por favor informe um código válido.")
        continue
    else:
        match (codigo):
            case 1: 
                qtd = int(input("Informe a quantidade de itens: "))
                valor = valor + (5 * qtd)
                continue
            case 2:
                qtd = int(input("Informe a quantidade de itens: "))
                valor = valor + (7 * qtd)
                continue
            case 3:
                qtd = int(input("Informe a quantidade de itens: "))
                valor = valor + (6 * qtd)
                continue
            case 4:
                print ("O valor total da sua compra foi: ", valor, "reais. Obrigado por comprar conosco!")
                break