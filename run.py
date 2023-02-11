from flask import Flask,jsonify,request,Blueprint
import os
import random
import json
import requests
import string
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy import text
import controllers.DesafioController as DesafiosController
import controllers.LinkedinController as LinkedinController
import controllers.JogadorController as JogadorController
import controllers.ProdutosController as ProdutosController
import controllers.MercadoController as MercadoController

from models.Tables import db, User
# from ln_oauth import auth, headers
from sqlalchemyseed import load_entities_from_json,Seeder

project_folder = os.path.expanduser(os.path.dirname(os.path.abspath(__file__)))  # adjust as appropriate

load_dotenv(os.path.join(project_folder, '.flaskenv'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

app.secret_key = os.environ.get("SESSION_SECRET")
app.config['SESSION_TYPE'] = 'filesystem'
db.init_app(app)
migrate = Migrate(app, db)

def seed():
    with app.app_context():
        try:
            user = User().query.first()
            # load entities
            if(user is None):

                entities = load_entities_from_json( 'seed.json')

                # Initializing Seeder
                seeder = Seeder(db.session())

                # Seeding
                seeder.seed(entities)

                # Committing
                db.session.commit()  # or seeder.session.commit()
        except Exception as e:
            output = str(e)
            is_database_working = False

seed()


linkedin_bp = Blueprint('linkedin_bp', __name__)

linkedin_bp.route('/', methods=['GET'])(LinkedinController.Linkedin_call)
linkedin_bp.route('/linkedin', methods=['GET'])(LinkedinController.login_linkedin)
linkedin_bp.route('/jogo', methods=['GET'])(LinkedinController.jogo)

app.register_blueprint(linkedin_bp, url_prefix='/')


Produtos_bp = Blueprint('Produtos_bp', __name__)

Produtos_bp.route('/', methods=['GET'])(ProdutosController.index)
Produtos_bp.route('/create', methods=['GET'])(ProdutosController.create)
Produtos_bp.route('/', methods=['POST'])(ProdutosController.store)
Produtos_bp.route('/<id>', methods=['GET'])(ProdutosController.show)
Produtos_bp.route('/<id>', methods=['POST'])(ProdutosController.update)
# Desafios_bp.route('/destroy/<id>', methods=['POST'])(ProdutosController.update)

app.register_blueprint(Produtos_bp, url_prefix='/produtos')

Desafios_bp = Blueprint('Desafios_bp', __name__)

Desafios_bp.route('/', methods=['GET'])(DesafiosController.index)
Desafios_bp.route('/painel', methods=['GET'])(DesafiosController.painel)
Desafios_bp.route('/create', methods=['GET'])(DesafiosController.create)
Desafios_bp.route('/', methods=['POST'])(DesafiosController.store)
Desafios_bp.route('/<id>', methods=['GET'])(DesafiosController.show)
Desafios_bp.route('/<id>', methods=['POST'])(DesafiosController.update)
# Desafios_bp.route('/destroy/<id>', methods=['POST'])(DesafiosController.update)

app.register_blueprint(Desafios_bp, url_prefix='/desafios')

Jogador_bp = Blueprint('Jogador_bp', __name__)

Jogador_bp.route('/historicos', methods=['GET'])(JogadorController.historicos)
Jogador_bp.route('/conquistas', methods=['GET'])(JogadorController.conquistas)
# Jogador_bp.route('/jogo', methods=['GET'])(JogadorController.jogo)

app.register_blueprint(Jogador_bp, url_prefix='/jogador')

Mercado_bp = Blueprint('Mercado_bp', __name__)

Mercado_bp.route('/', methods=['GET'])(MercadoController.index)
#Mercado_bp.route('/conquistas', methods=['GET'])(MercadoController.conquistas)
# Mercado_bp.route('/jogo', methods=['GET'])(MercadoController.jogo)

app.register_blueprint(Mercado_bp, url_prefix='/mercado')