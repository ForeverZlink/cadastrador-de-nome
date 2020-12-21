from  modules import  cosmetic,analise


while True:
    cosmetic.tabela()
    choice=analise.test_choice()
    if choice == 4:
        break
    else:
        with open('pessoas_cadastradas.txt','a+') as pes:
            if choice==1:
                cosmetic.linha()
                print('Pessoas:')
                pes.seek(0,0)
                print(pes.read(),end='')
            elif choice==3:
                print('\033[31mAinda não disponivel (:(')
            else:
                nome_da_pessoa=str(input('Digite o nome da pessoa:'))
                idade_da_pessoa=analise.leia_int()
                pes.write(f'Nome:{nome_da_pessoa}, Idade:{idade_da_pessoa}\n')

print('>>Fim de Programa<<')
