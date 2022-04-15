from time import sleep

def menu():
    """
    -> apenas para mostrar o menu de opções
    """
    sleep(1)
    print("\033[35m==" * 25)
    print("\033[33m{:^50}".format('MENU PRINCIPAL'))
    print("\033[35m==" * 25)
    print('\033[33m1 - \033[34mVer pessoas cadastradas')
    print('\033[33m2 - \033[34mCadastrar novas pessoas')
    print('\033[33m3 - \033[34mSair do sistema')
    print("\033[35m==" * 25)
    n = leiaInt('\033[33mSua opção: ')
    return n


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except UnboundLocalError: 
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("\033[31mA leitura de dados foi interrompida pelo usuário")
        else:
            if n == 1 or n == 2 or n == 3:
                return n
            else:
                print('\033[31mERRO: o valor nao corresponde a uma das opções:')


def leiaInt2(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("\033[31mA leitura de dados foi interrompida pelo usuário")
        else:
            return n
            

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: o valor nao corresponde a um numero")
        except KeyboardInterrupt:
            print("\033[31mA leitura de dados foi interrompida pelo usuário")
        else:
            return n
            

def pessoas():
    sleep(1)
    print("\033[35m==" * 25)
    print("\033[33m{:^50}".format("PESSOAS CADASTRADAS"))
    print("\033[35m==" * 25)
    print("\033[4;33mNOME           | NASCIMENTO  | PESO  | CONTATO    \033[m")
    print()


def cadastrar():
    sleep(1)
    print("\033[35m==" * 25)
    print("\033[33m{:^50}".format("CADASTRAR NOVAS PESSOAS"))
    print("\033[35m==" * 25)


def sair():
    sleep(1)
    print("\033[35m==" * 25)
    print("\033[33m{:^50}".format("SAINDO DO SISTEMA... ATÉ LOGO!"))
    print("\033[35m==" * 25)
    print('\033[m', end= '')


