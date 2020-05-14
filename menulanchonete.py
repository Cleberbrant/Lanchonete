from os import system
from time import sleep

question = 0
valorHamburguer = 0
valorBebida = 0
resultado = 0
while question != 4:
    system("cls")
    print("=========== MENU ===========")
    print('''[1] Hamburgues.
[2] Bebidas.
[3] Valor da conta.
[4] Finalizar pedido. ''')
    print("=========== MENU ===========")
    question = int(input('>>>>>> Qual é a sua opção ? '))

    if question == 1:
        print('''======== Hamburgues ======== 
[1] R$ 10,00 - X-Bacon.
[2] R$ 14,90 - X-Bacon Duplo.
[3] R$ 19,90 - X-Picanha.
[4] Voltar ao menu principal.
======== Hamburgues ======== ''')
        while question == 1:
            hamburguer = int(input("Escolha um Hamburguer, ou volte ao menu incial: "))
            if hamburguer == 1:
                print("X-Bacon foi adicionado ao carrinho com sucesso ! ")
                valorHamburguer = valorHamburguer + 10.00
            elif hamburguer == 2:
                print("X-Bacon Duplo foi adicionado ao carrinho com sucesso ! ")
                valorHamburguer = valorHamburguer + 14.90
            elif hamburguer == 3:
                print("X-Picanha foi adicionado ao carrinho com sucesso ! ")
                valorHamburguer = valorHamburguer + 19.90
            elif hamburguer == 4:
                break
    elif question == 2:
        print('''======== Bebidas ======== 
[1] R$ 4,00 - Coca Cola.
[2] R$ 4,50 - Suco de Laranja.
[3] R$ 6,00 - Cerveja Litrão.
[4] Voltar ao menu principal.
======== Bebidas ======== ''')
        while question == 2:
            bebida = int(input("Escolha sua bebida, ou volte ao menu incial: "))
            if bebida == 1:
                print("Coca Cola foi adicionada ao carrinho com sucesso !")
                valorBebida = valorBebida + 4.00
            elif bebida == 2:
                print("Suco de Laranja foi adicionado ao carrinho com sucesso !")
                valorBebida = valorBebida + 4.50
            elif bebida == 3:
                print("Suco de Laranja foi adicionado ao carrinho com sucesso !")
                valorBebida = valorBebida + 6.00
            elif bebida == 4:
                break

    elif question == 3:
            resultado = valorHamburguer + valorBebida
            print("Valor da conta R${:.2f}".format(resultado))
            sleep(3)
    elif question == 4:
        print("O seu pedido foi feito =D")
        break