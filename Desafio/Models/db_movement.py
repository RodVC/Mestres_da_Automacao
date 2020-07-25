import sqlalchemy
from sqlalchemy import create_engine # função que ajuda a criar o BD
from sqlalchemy.orm import sessionmaker #pra poder conectar ao BD
from Models.db_models import Produtos
from Models.base import Base


def configurar_banco_de_dados(): #TEM QUE SER IMPORTADA NO MÓDULO 
    engine = create_engine('sqlite:///db_produtos.db', echo=True)
    # Base.metadata.drop_all(bind=engine) # Serve para apagar todas as tabelas
    Base.metadata.create_all(bind=engine)
    Conexao = sessionmaker(bind=engine)
    conexao = Conexao()
    conexao: sessionmaker
    return conexao

def add_produtos(conexao, nome, preco, descricao): #TEM QUE SER IMPORTADA NO MÓDULO PRINCIPAL
    novo_produto = Produtos()
    novo_produto.nome_produto = nome
    novo_produto.preco_produto = preco
    novo_produto.desc_produto = descricao
    conexao.add(novo_produto)
    conexao.commit()

def buscar_todos_produtos(conexao):
    consulta = conexao.query(Produtos).all()
    for linha in consulta:
        print(linha.nome_produto, linha.preco_produto, linha.desc_produto)