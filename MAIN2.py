import smurf as s
from time import sleep
cliente = {} 

while True:
    s.menu()
    opcao = s.opcao('Sua opção: ')
    if opcao == 1:
        
        s.cadastradas(cliente)
        sleep(2)
        
        
    elif opcao == 2:
        s.cadastrar(cliente)
        
        
        

    elif opcao == 3:
        print('Saindo do sistema...')
        break

    elif opcao == 4:
        try:
            escolha = str(input('Realmente deseja limpar os dados?(s/n)'))
            
            if escolha.lower() == 's':
                s.limpar()
                    
            
            elif escolha.lower() == 'n':
                print('Ok, arquivo sem mudanças.')
        except:
            print('erro')
        
        
    else:
        print('-'*30)
        print('ERRO, DIGITE UMA DAS OPÇÕES.')
        print('-'*30)
        sleep(2)


