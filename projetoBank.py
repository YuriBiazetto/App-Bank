from time import sleep
from random import randint

#função de saque
def saque(saldo):
    vlr_saque = float(input('Digite o valor para saque: R$ '))
    conf = str(input('Confirmar valor de saque? (S - sim, N - não)\n')).strip().upper()
    if conf == 'S':
        if saldo < vlr_saque:
            print('Operação não realizada\nSaldo insuficiente!')
            opcoes(saldo)
        else:
            saldo -= vlr_saque
            print('Saque realizado com sucesso!')
            print(saldo)
            opcoes(saldo)
    elif conf == 'N':
        print('Operação cancelada!')
        opcoes(saldo)

#função de deposito
def deposito(saldo):
    vlr_depositado = float(input('Digite o valor a ser depositado: R$ '))
    conf = str(input('Confirmar valor de deposito? (S - sim, N - não)\n')).strip().upper()
    if conf == 'S':
        saldo += vlr_depositado
        print('Valor depositado em sua conta!')
        opcoes(saldo)
    elif conf == 'N':
        print('Operação cancelada!')
        opcoes(saldo)

#função de extrato
def extrato(saldo):
    print(f'\nSaldo em conta: R$ {saldo:.2f}')
    x = str(input('Voltar ao menu principal? (S - sim, N - não) ')).strip().upper()

    if x == 'S':
        opcoes(saldo)
    else:
        print('Até logo')

#função de opcoes
def opcoes(saldo, nome):
    print(f'''\n
Bem vindo {nome}!
Escolha a opção desejada:
1 - Saque
2 - Depósito
3 - Extrato
4 - Sair''')
    n = int(input())
    if n == 1:
        saque(saldo)
    elif n == 2:
        deposito(saldo)
    elif n == 3:
        extrato(saldo)
    elif n == 4:
        print("Até logo")
        sleep(3)
        exit()
    else:
        print('Escolha inválida!')
        opcoes(saldo)

#login
def login(dados_prontos):
    print('Login')
    sleep(1)
    conta = int(input("Conta: "))
    senha = int(input('Senha: '))
    if conta == dados_prontos['cadConta'] and senha == dados_prontos['cadSenha']:
        saldo = 0  # Inicializar o saldo
        opcoes(saldo)
    else:
        x = int(input('\nLogin ou senha inválidos.\n1 - Tentar novamente\n2 - Criar conta\n3 - Sair\n'))
        if x == 1:
            login(dados_prontos)
        elif x == 2:
            criar_conta()
        else:
            print('Saindo...')
            sleep(2)

#criar nova conta
def criar_conta():
    print('Criação de Nova Conta')
    sleep(1)
    nome = input('Nome completo: ').strip().upper()
    data_nasc = input('Data de nascimento (dd/mm/aaaa): ')
    rua = input('Logradouro: ').strip().upper()
    num = int(input('Número: '))
    cid_uf = input('Cidade - UF: ').strip().upper()
    cadSenha = input('Crie sua senha: ').strip()
    cadSenha2 = input('Confirme sua senha: ').strip()
    
    while cadSenha != cadSenha2:
        print("As senhas não coincidem. Tente novamente.")
        cadSenha = input('Crie sua senha: ').strip()
        cadSenha2 = input('Confirme sua senha: ').strip()
    
    cadAgencia = randint(100, 999)
    cadConta = randint(1, 99999)
    dados_prontos = {
        'nome': nome,
        'data_nasc': data_nasc,
        'rua': rua,
        'numero': num,
        'cid_uf': cid_uf,
        'cadAgencia': cadAgencia,
        'cadConta': cadConta,
        'cadSenha': cadSenha
    }
    print(f'Agencia: {cadAgencia}\nConta: {cadConta}')
    return dados_prontos

#main
def main():
    print('***** Banco Nacional *****')
    print('Seja bem vindo ao Banco Nacional!\nFaça seu login para continuar.')

    escolha = int(input('1 - Nova conta\n2 - Acessar sua conta\n'))
    if escolha == 1:
        dados_prontos = criar_conta()
        login(dados_prontos)
    elif escolha == 2:
        # Aqui você pode carregar os dados da conta de um banco de dados ou outro meio
        dados_prontos = {'nome': 'Cleber', 'data_nasc': '20/11/2000', 'rua': 'Independente', 'numero': 12, 'cid_uf': 'Osasco - SP', 'cadAgencia': 123, 'cadConta': 12345, 'cadSenha': 321}
        login(dados_prontos)
    else:
        print('Escolha inválida!')

main()