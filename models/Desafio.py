from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    __tablename__ = 'users'

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