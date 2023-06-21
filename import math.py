import math



while True:

    print("MENU:")

    print("1. Calcular a soma das raízes quadradas de dois números")

    print("2. Apresentar na tela uma tabela de potências de 0 a 10")

    print("3. Arredondar número para cima")

    print("4. Sair")

    print("OPÇÃO: ____")

    x = int(input())



    if x == 1:

        n1 = int(input("Digite um número: "))

        n2 = int(input("Digite um número: "))

        

        raiz1 = math.sqrt(n1)

        raiz2 = math.sqrt(n2)

        

        soma = raiz1 + raiz2

        print("A soma das raízes quadradas é:", soma)



    elif x == 2:

        n1 = int(input("Digite um número: "))

        

        for i in range(11):

            result = n1 ** i

            print(n1, "**", i ,"=", result)



    elif x == 3:

        n = float(input("Digite um número: "))

        arredondado = math.ceil(n)

        print("O número arredondado para cima é:", arredondado)



    elif x == 4:

        break

    else:

        print("Opção inválida. Por favor, escolha uma opção válida.")

