from dependências.funções import *

def ArquivoExist(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
  
    
def Criar_Arq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def LerArquivo(arq):
    try:
        a = open(arq, "rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        pessoas()
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<15}| {dado[1]:<4}| {dado[2]:<12}| {dado[3]:<6}| {dado[4]}\033[m", end='')
            
    finally:
        a.close()
    
def cadastro(arq, nome, sexualidade, nascimento, peso, contato):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro ao carregar o arquivo!")
    else:
        try:
            a.write(f"{nome};{sexualidade};{nascimento};{peso};{contato}\n")
        except:
            print("Houve um erro ao carregar o arquivo")
        else:
            print(f'Novo registro de \'{nome}\' adicionado.')
            a.close()


