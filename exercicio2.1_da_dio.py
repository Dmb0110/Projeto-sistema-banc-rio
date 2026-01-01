from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente: Cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod    
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero   # corrigido

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):      # corrigido
        return self._historico
    
    def sacar(self, valor):
        if valor > self._saldo:
            print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')
            return False
        elif valor > 0:
            self._saldo -= valor
            print('\n=== Saque realizado com sucesso! ===')
            return True
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
            return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n=== Depósito realizado com sucesso! ===')
            return True
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [t for t in self.historico.transacoes if t['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques   # corrigido

        if excedeu_limite:
            print('\n@@@ Operação falhou! O valor do saque excede o limite. @@@')
            return False
        elif excedeu_saques:
            print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')
            return False
        else:
            return super().sacar(valor)
    
    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
"""


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(   # corrigido
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),  # corrigido
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


cliente1 = PessoaFisica(
    cpf='12345678900',
    nome='maria silva',
    data_nascimento='01-01-1990',
    endereco='Rua das flores,123 - centro - Rio de Janeiro/RJ'
)

conta1 = ContaCorrente.nova_conta(cliente=cliente1, numero=1)
cliente1.adicionar_conta(conta1)

deposito = Deposito(500)
cliente1.realizar_transacao(conta1,deposito)

saque = Saque(200)
cliente1.realizar_transacao(conta1,saque)

for transacao in conta1.historico.transacoes:
    print(transacao)

print('Saldo:',conta1.saldo)
