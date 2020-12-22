def test_choice(text='Qual é sua escolha?'):
    while True:
        try:
            numero = int(input(text))
        except:
            print('Digite apenas o números:1, 2, 3 ou 4.')
        else:
            if numero> 0 and numero<5:
                return numero
            else:
                print('Apenas: 1,2,3 ou 4')


def leia_int(pergunta='Digite a idade da pessoa:'):
    while True:
        try:
            num=int(input(pergunta))
        except:
            print('Digite apenas números inteiros')

        else:
            if num<121:
                return num