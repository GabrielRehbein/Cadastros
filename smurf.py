import pandas as pd

def menu():
    print('-'*30)
    print('        MENU PRINCIPAL')
    print('-'*30)
    print('[1] - Ver pessoas cadastradas\n[2] - Cadastrar nova pessoa\n[3] - Sair do sistema\n[4] - Limpar Base de Dados')


def opcao(num):
    while True:
        try:
            escolha = int(input(num))
        except:
            print('ERRO. Digite uma das opções.')
            
        else:
            return escolha


def cadastradas(cliente):
    print('-'*30)
    print('     PESSOAS CADASTRADAS')
    print('-'*30)
    with open('pessoas.txt', 'r') as arquivo:
        ler = arquivo.read()
        ler = ler.replace(',', '  --- ')
        print(ler)
        
            

    
  
    

def cadastrar(cliente):

    
    while True:
        try:
            nome = str(input('Nome: ')).lower()
            
        except:
            print('Digite um valor valido:')
            continue   
        try:   
            idade = int(input('Idade: '))
        except:
            print('Digite um valor valido:')
            continue 
        try:   
            cpf = str(input('CPF(somente numeros): '))
            
            
            if len(cpf) != 11:
                print('Cpf invalido.')
                continue
            
            
            
                
        except:
            print('Digite algo válido.')
            continue 
        with open('pessoas.txt', 'r') as ler:
            if cpf in ler.read():
                    print('Cliente já cadastrado.')
                
                    break 
        
        confirmar = str(input('Confirma o cadastro (s/n): ')).lower()
        
        if confirmar == 'n':
            print('-'*30)
            print('CLIENTE NÃO CADASTRADO')
            break
            
        
        else:
            print('-'*30)
            print('CLIENTE CADASTRADO')
            print('-'*30)
            with open('pessoas.txt', 'a') as arquivo:
                
                arquivo.write(nome) and arquivo.write(',') and arquivo.write(str(idade)) and arquivo.write(',') and arquivo.write(cpf) and arquivo.write('\n') 
                   
            sair = str(input('Digite "s" para sair: ')).lower()
            if sair == 's':
                
                break
            else:
                continue
            
def limpar():
    print('Arquivo limpo.')
    with open('pessoas.txt', 'w') as arquivo:
        arquivo.write('nome,idade,cpf\n')
    

# def voltar_menu():
#     voltar_menu = str(input('Deseja voltar ao menu(s/n): ')).lower()
    
        
#     if voltar_menu == 'n':
        
#         print('Saindo do sistema...')
        
        
            