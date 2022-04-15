from dependências.funções import *
from dependências.arquivo import *
from datetime import *

# programa principal

# Verifica se o arquivo existe, se não, o arquivo é criado
arq = 'Dados cadastrais'
if not ArquivoExist(arq):
    Criar_Arq(arq)

while True:
    n = menu()
    if n == 1:
        # opção para ler um arquivo
        LerArquivo(arq)
    if n == 2:
        # opção para cadastrar novas pessoas
        cadastrar()
        nome = str(input('\033[32mDigite o nome: '))
        dia = leiaInt2('Informe o dia do seu nascimento: ')
        mes = leiaInt2('Informe o mes do nascimento: ')
        ano = leiaInt2('Informe o ano do nascimento: ')
        peso = LeiaFloat('Informe seu peso: ')
        contato = leiaInt2('Informe um número para contato: ')
        nascimento = str(f'{dia}/{mes}/{ano}')

        # calculando a idade

        dat_nasc = date(ano, mes, dia)
        nasc = date.today() - datnasc
        calculo_idade = nasc.days / 365.25
        idade = int(calculo_idade)


        cadastro(arq, nome, nascimento, peso, contato)

    if n == 3:
        sair()
        break
