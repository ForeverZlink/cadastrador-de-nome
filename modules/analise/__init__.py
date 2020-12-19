def test_choice(text='Qual é sua escolha?'):
    while True:
        try:
            numero=int(input(text))
        except:
            print('Digite apenas o número 1,2 ou 3.')
        else:
            if numero> 0 and numero<4:
                return numero
            else:
                print('Apenas 1,2 ou 3')
            