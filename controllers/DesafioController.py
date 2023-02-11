# from flask import jsonify,request
import os
import random
import json
import requests
import string

import sys
from flask import render_template, redirect, url_for, request, abort, session
from models.Tables import db, Desafio

# from ln_oauth import auth, headers
def painel():
    desafios = Desafio.query.order_by(Desafio.id).all()
    return render_template('desafio/painel.html',desafios=desafios)
    return 'index'

# from ln_oauth import auth, headers
def index():
    desafios = Desafio.query.order_by(Desafio.id).all()
    return render_template('desafio/index.html',desafios=desafios)
    return 'index'

def show():
    desafio = Desafio().query.filter_by(id=id).first()
    return render_template('desafios/form.html',desafio=desafio)
    return 'show'

def update():
    data = request.form
    produto = Produto.query.filter_by(id='id').update(
            id=data['id'],
            titulo =data['titulo'],
            moedas =data['moedas'],
            data_inicio =data['data_inicio'],
            data_final =data['data_final'],
            grupo =data['grupo'],
            categoria =data['categoria'],
            situacao =data['situacao'],
            banner =data['banner'],
            card =data['card']
    )
    db.session.add(produto)
    db.session.commit()
    return redirect('/desafios')
    return 'update'

def create():
    desafio = Desafio()
    return render_template('desafio/form.html',desafio=desafio)
    return 'create'

def store():
    data = request.form
    desafio = Desafio(
            titulo =data['titulo'],
            moedas =data['moedas'],
            data_inicio =data['data_inicio'],
            data_final =data['data_final'],
            grupo =data['grupo'],
            categoria =data['categoria'],
            situacao =data['situacao'],
            #banner =data['banner'],
            #card =data['card']
    )
    db.session.add(desafio)
    db.session.commit()
    return redirect('/desafios')
    return 'store'

def destroy():
    desafio = Desafio().query.filter_by(id=id).first()
    db.session.delete(desafio)
    db.session.commit()
    return redirect('/desafios')
    return 'destroy'