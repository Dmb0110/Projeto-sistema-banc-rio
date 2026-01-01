
'''
import os
import shutil
from pathlib import Path

#arquivo = open('novo-arquivo.txt')

#print(__file__)

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / 'novo-diretorio3')

#os.rename(ROOT_PATH / 'rascunho6.txt',ROOT_PATH / 'alterado3.txt')

#os.remove(ROOT_PATH / 'alterado3.txt')

shutil.move(ROOT_PATH / 'rascunho1.txt', ROOT_PATH / 'exercicio' / 'rascunho1.txt')
'''
from http.client import HTTPException

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Produto:
    id: int
    nome: str
    preco: int

lista: List[Produto] = []

@app.post('/enviar')
def criar(produto: Produto)
    lista.append(produto)
    return {'mensagem':'Produto adicionado com sucesso'}

@app.get('/receber')
def receber():
    return lista

@app.put('/trocar')
def trocar(id: int,at_produto: Produto):
    for index,produto in enumerate(lista):
        if produto.id == id:
            lista[index] = at_produto
            return at_produto
    raise HTTPException(status_code=404,detail='produto nao encontrado')


@app.patch("/atualizar")
def atualizar(id: int, nome: str = None, preco: float = None):
    for index, produto in enumerate(lista):
        if produto.id == id:
            # Atualiza apenas os campos enviados
            if nome is not None:
                lista[index].nome = nome
            if preco is not None:
                lista[index].preco = preco
            return {"mensagem": "Produto atualizado parcialmente!", "produto": lista[index]}
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.delete('/deletar')
def deletar(id: int):
    for index,produto in enumerate(lista):
        if produto.id == id:
            del lista[index]
            return {'mensagem':'Produto deletado com sucesso'}
    raise HTTPException(status_code=404,detail='produto nao encontrado')
