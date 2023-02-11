# from flask import jsonify,request
import os
import random
import json
import requests
import string

import sys
from flask import render_template, redirect, url_for, request, abort, session
from models.Tables import db, Carteira, CarteiraHistorico, Conquista, UserConquista, Produto

# from ln_oauth import auth, headers
def index():
    produtos = Produto.query.filter_by(ativo=1).all()
    #historicos = CarteiraHistorico.query.filter_by(carteira_id=carteira.id).order_by(CarteiraHistorico.created_at).all()
    return render_template('mercado/index.html',produtos=produtos)
    return 'index'

def conquistas():
    conquistas = Conquista().query.all()
    return render_template('jogador/conquistas.html',conquistas=conquistas)
    return 'show'

def create():
    produto = Produto()
    return render_template('produtos/form.html',produto=produto)

    return 'create'

def destroy():
    produto = Produto().query.filter_by(id=id).first()
    db.session.delete(produto)
    db.session.commit()
    return redirect('/produtos')
    return 'destroy'