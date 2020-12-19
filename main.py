from  modules import  cosmetic,analise



while True:
    cosmetic.tabela()
    choice=analise.test_choice()
    if choice ==3:
        break
    else:
        with open('pessoas_cadastradas.txt','a+') as pes:
            if choice==1:
                cosmetic.linha()
                print('Pessoas:')
                pes.seek(0,0)
                print(pes.read(),end='')
            else:
                nome_da_pessoa=str(input('Digite o nome da pessoa:'))+'\n'
                pes.write(nome_da_pessoa)

print('>>Fim de Programa<<')
