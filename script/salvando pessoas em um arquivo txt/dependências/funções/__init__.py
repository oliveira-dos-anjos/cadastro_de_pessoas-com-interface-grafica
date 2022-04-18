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


def leiaCont(msg):
    while True:
        try:
            n = int(input(msg))
            contato = str(n)
        except (ValueError, TypeError):
            print("ERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("A leitura de dados foi interrompida pelo usuário")
        else:
            if len(contato) <=9:
                print("os dados nao correspondem a um número telefônico")
            else:
                return n
            

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


def calculo_idade(a, m, d):
    while True:
        try:
            dat_nasc = date(a, m, d)
            nasc = date.today() - dat_nasc
            calculo_idade = nasc.days / 365.25
            idade = int(calculo_idade)
            nascimento = str(f"{d}/{m}/{a}")
        except:
            print("Algumas informações de nascimento ficaram erradas: ")
            d = leiaDia('Informe o dia do seu nascimento: ')
            m = leiaMes('Informe o mes do nascimento: ')
            a = leiaAno('Informe o ano do nascimento: ')
            nascimento = calculo_idade(a, m, d)
        else:
            return nascimento


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(",", "."))
        except (ValueError, TypeError):
            print("ERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("A leitura de dados foi interrompida pelo usuário")
        else:
            return f'{n:.1f}'
            

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
