opcao = 0
saldo = 0
extrato = ''

def menu():
    '''
    menu = 
    ----------------MENU-----------------
    [ d ] Depositar
    [ s ] Sacar
    [ e ] Extrato
    [ nc ] Nova conta
    [ lc ] Listar contas
    [ nu ] Novo usuario
    [ q ] Sair
    '''
    print('[1] depositar')
    print('[2] sacar')
    print('[3] extrato')
    print('[4] nova conta')
    print('[5] listar contas')
    print('[6] novo usuario')
    print('[0] sair')
    opcao = input('escolha a operaçao desejada: ')

def main():
    global saldo,extrato
    menu()
    if opcao == 1:
        deposito = float(input('quanto quer depositar: '))
        saldo += deposito
        extrato = f'o valor depositado e: {deposito}'
    return saldo,extrato


main()
