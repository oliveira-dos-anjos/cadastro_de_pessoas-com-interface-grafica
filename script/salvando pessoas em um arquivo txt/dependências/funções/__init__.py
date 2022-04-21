from time import sleep
from datetime import *

def menu():
    """
    -> apenas para mostrar o menu de opções
    """
    sleep(1)
    print("==" * 28)
    print("{:^56}".format('MENU PRINCIPAL'))
    print("==" * 28)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar novas pessoas')
    print('3 - Sair do sistema')
    print("==" * 28)
    n = leiaInt('Sua opção: ')
    return n


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: o valor nao corresponde a um numero")
        except UnboundLocalError: 
            print("ERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("A leitura de dados foi interrompida pelo usuário")
        else:
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                print('ERRO: o valor nao corresponde a uma das opções:')



            

def leiaDia(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("A leitura de dados foi interrompida pelo usuário")
        else:
            if n >= 32:
                print('A data nao corresponde ao dias de um mês:')
            else:    
                return n
                       

def leiaMes(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("A leitura de dados foi interrompida pelo usuário")
        else:
            if n <= 0 or n >= 13:
                print('O valor nao corresponde a um mês:')
            else:    
                return n
            

def leiaAno(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("A leitura de dados foi interrompida pelo usuário")
        else:
            return n





def pessoas():
    sleep(1)
    print("==" * 28)
    print("{:^56}".format("PESSOAS CADASTRADAS"))
    print("==" * 28)
    print("NOME           | SEXO| NASCIMENTO  | PESO  | CONTATO    ")
    print("__" * 28)


def cadastrar():
    sleep(1)
    print("==" * 28)
    print("{:^56}".format("CADASTRAR NOVAS PESSOAS"))
    print("==" * 28)



def sair():
    sleep(1)
    print("==" * 28)
    print("{:^56}".format("SAINDO DO SISTEMA... ATÉ LOGO!"))
    print("==" * 28)
    print('', end= '')


def leiasexo(msg):
    while True:
        s = str(input(msg)).upper().strip()
        if s == "F" or s == "M":
            s = str(r)
            break
        
        else:
            print("Apenas 'F' ou 'M': ")
    return s
