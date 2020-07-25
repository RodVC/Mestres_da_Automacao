import sqlalchemy
from sqlalchemy import Column # Ajuda a definir propriedades de uma coluna
from sqlalchemy import Integer# Tipo que será utilizado dentro de uma coluna
from sqlalchemy import String# Tipo que será utilizado dentro de uma coluna
from sqlalchemy import Numeric# Tipo DECIMAL que será utilizado dentro de uma coluna
from sqlalchemy import Sequence# Para habilitar o autoincrement
from sqlalchemy import ForeignKey# Para habilitar chave estrangeira
from sqlalchemy.orm import relationship #pra poder conectar ao BD
from Models.base import Base

class Produtos(Base): # se usa a função aqui como parâmetro para que esta class vire uma tabela
    __tablename__ = 'produtos'
    produto_id = Column(Integer, Sequence('produto_id_autoincremento',start=1), primary_key= True)
    nome_produto = Column(String)
    preco_produto = Column(Numeric(10,2))
    desc_produto = Column(String)