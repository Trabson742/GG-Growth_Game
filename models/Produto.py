from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    valor = db.Column(db.String(120))
    marca = db.Column(db.String(120))
    modelo = db.Column(db.String(120))
    categoria = db.Column(db.String(120))
    ano = db.Column(db.String(120))
    quantidade_estoque = db.Column(db.String(120))
    descricao = db.Column(db.text)
    imagem = db.Column(db.String(120))
    ativo = db.Column(db.BOOLEAN)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome' : self.nome,
            'valor' : self.valor,
            'marca' : self.marca,
            'modelo' : self.modelo,
            'categoria' : self.categoria,
            'ano' : self.ano,
            'quantidade_estoque' : self.quantidade_estoque,
            'descricao' : self.descricao,
            'imagem' : self.imagem,
            'ativo' : self.ativo
        }