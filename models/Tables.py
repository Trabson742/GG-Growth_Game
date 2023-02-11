from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    # email = db.Column(db.String(120))
    avatar = db.Column(db.String(120))
    linkedin_id = db.Column(db.String(40))

    carteira = db.relationship('Carteira', backref='users', lazy=True)
    conquistas = db.relationship('UserConquista', backref='users', lazy=True)
    desafios = db.relationship('UserDesafio', backref='users', lazy=True)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            # 'email': self.email,
            'avatar': self.avatar,
            'linkedin_id': self.linkedin_id
        }


class Desafio(db.Model):
    __tablename__ = 'desafios'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120))
    moedas = db.Column(db.String(120))
    data_inicio = db.Column(db.Date)
    data_final = db.Column(db.Date)
    grupo = db.Column(db.String(120))
    categoria = db.Column(db.String(120))
    situacao = db.Column(db.String(120))
    banner = db.Column(db.String(120))
    card = db.Column(db.TEXT)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'titulo' : self.titulo,
            'moedas' : self.moedas,
            'data_inicio' : self.data_inicio,
            'data_final' : self.data_final,
            'grupo' : self.grupo,
            'categoria' : self.categoria,
            'situacao' : self.situacao,
            'banner' : self.banner,
            'card' : self.card
        }

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120))
    preco = db.Column(db.String(120))
    preco_desconto = db.Column(db.String(120))
    marca = db.Column(db.String(120))
    modelo = db.Column(db.String(120))
    categoria = db.Column(db.String(120))
    ano = db.Column(db.String(120))
    quantidade_estoque = db.Column(db.String(120))
    descricao = db.Column(db.TEXT)
    imagem = db.Column(db.String(120))
    ativo = db.Column(db.BOOLEAN)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome' : self.nome,
            'preco' : self.preco,
            'preco_desconto' : self.preco_desconto,
            'marca' : self.marca,
            'modelo' : self.modelo,
            'categoria' : self.categoria,
            'ano' : self.ano,
            'quantidade_estoque' : self.quantidade_estoque,
            'descricao' : self.descricao,
            'imagem' : self.imagem,
            'ativo' : self.ativo
        }

class Conquista(db.Model):
    __tablename__ = 'conquistas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120))
    moedas = db.Column(db.String(120))
    dificuldade = db.Column(db.String(120))
    descricao = db.Column(db.TEXT)
    insignia = db.Column(db.String(120))
    historico = db.relationship('UserConquista', backref='conquista', lazy=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'titulo' : self.titulo,
            'moedas' : self.moedas,
            'dificuldade' : self.dificuldade,
            'descricao' : self.descricao,
            'insignia' : self.insignia
        }

class Carteira(db.Model):
    __tablename__ = 'carteira'

    id = db.Column(db.Integer, primary_key=True)
    moedas = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)    
    conquistas = db.Column(db.Integer)
    updated_at = db.Column(db.Date)
    historico = db.relationship('CarteiraHistorico', backref='cateira', lazy=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id' : self.user_id,
            'moedas' : self.moedas,
            'conquistas' : self.conquistas,
        }

class UserConquista(db.Model):
    __tablename__ = 'user_conquistas'

    id = db.Column(db.Integer, primary_key=True)
    conquista_id = db.Column(db.Integer, db.ForeignKey('conquistas.id'),
        nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)    
    created_at = db.Column(db.Date)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id' : self.user_id,
            'conquista_id' : self.conquista_id,
            'created_at' : self.created_at,
        }

class UserDesafio(db.Model):
    __tablename__ = 'user_Desafios'

    id = db.Column(db.Integer, primary_key=True)
    desafio_id = db.Column(db.Integer, db.ForeignKey('desafios.id'),
        nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)    
    created_at = db.Column(db.Date)
    ended_at = db.Column(db.Date)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id' : self.user_id,
            'desafio_id' : self.desafio_id,
            'created_at' : self.created_at,
        }

class CarteiraHistorico(db.Model):
    __tablename__ = 'carteira_historicos'

    id = db.Column(db.Integer, primary_key=True)
    carteira_id = db.Column(db.Integer, db.ForeignKey('carteira.id'),
        nullable=False)    
    moedas = db.Column(db.Integer)
    evento = db.Column(db.TEXT)  
    created_at = db.Column(db.Date)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'carteira_id' : self.carteira_id,
            'evento' : self.evento,
            'moedas' : self.moedas,
            'created_at' : self.created_at,
        }

