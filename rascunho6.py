'''
o decorador deve registrar o seguinte para chamada de funçao:
1 Data e hora atuais

2 Nome da funçao

3 Argumentos da funçao

4 Valor retornado pela funçao

5 O arquivo de log deve ser chamado log.txt

6 Se o arquivo log.txt ja existir,
os novos logs devem ser adicionados ao final do arquivo

7 Cada entrada de log deve estar em nova linha

(no desafio do derenciamento de pacontes tem que usar)
black,flake8,isort






class Produto:
    def __init__(self):
        self.lista = []

    def adicionar_produto(self,nome,preco):
        self.lista.append({'nome':nome,'preco':preco})

    def listar_produtos(self):
        for p in self.lista:
            print(f'{p['nome']},{p['preco']}')

    def trocar_produto(self,nome_antigo,nome_novo,preco_novo):
        for p in self.lista:
            if p['nome'] == nome_antigo:
                p['nome'] = nome_novo
                p['preco'] = preco_novo
                break

    def apagar_produto(self):
        self.lista = [p for p in self.lista if p['nome'] != nome]


p1 = Produto()

p1.adicionar_produto('arroz',20)

p1.adicionar_produto('batata',15)

p1.listar_produtos()
'''

class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('bom ,bom...')

    def parar(self):
        print('parando bicicleta...')
        print('bicicleta parada')

    def correr(self):
        print('vrummmm...')


b1 = Bicicleta('vermelha','caloi',2022,600)

b1.buzinar()
b1.parar()
b1.correr()