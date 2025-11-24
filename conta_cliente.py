import textwrap

def menu():
    menu = '''
    ----------------MENU-----------------
    [ d ] Depositar
    [ s ] Sacar
    [ e ] Extrato
    [ nc ] Nova conta
    [ lc ] Listar contas
    [ nu ] Novo usuario
    [ q ] Sair
    '''
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R${valor:.2f}\n'
        print(f'Deposito de R${valor} realizado com sucesso')
    else:
        print('operaçao falhou,o valor informado e invalido')

    return saldo,extrato

def sacar(*,saldo,valor,extrato,limite,numero_saque,limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque

    if excedeu_saldo:
        print('\n Operaçao falhou,Voce nao tem saldo suficiente.')

    if excedeu_limite:
        print('\n Operaçao falhou,O valor do saque excede o limite.')

    elif excedeu_saques:
        print('\n Operaçao falhor,Numero maximo de saques excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        numero_saque += 1
        print('\n ---Saque realizado com sucesso---')

    else:
        print('\n Operaçao falhou,O valor informado e invalido.')

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print('\n------------- EXTRATO -----------------')
    print('Nao foram realizadas movimentaçoes.'if not extrato else extrato)
    print(f'\nSaldo:\t\tR${saldo:.2f}')
    print('-----------------------------------------')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente numero): ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n Ja existe usuario com esse CPF.')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa):')
    endereço = input('Informe o endereço (logradouro,nro - bairro - cidade/sigla estado):')

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento,'cpf':cpf,'endereço':endereço})

    print('--- Usuario criado com sucesso ---')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n--- Conta criada com sucesso ---')
        return {'agencia':agencia,'numero_conta':numero_conta,'usuario':usuario}

    print('\n Usuario nao encontrado,fluxo de criaçao de conta encerrada.')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agencia:\{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('-' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu().strip()

        if opcao == 'd':
            valor = float(input('Informe o valor do deposito: '))

            saldo,extrato = depositar(saldo,valor,extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE,
            )

        elif opcao == 'e':
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print(f'DEBUG: "{opcao}"(len={len(opcao)})')
            print('Operaçao invalida,por favor selecione novamente a operaçao desejada.')


main()
