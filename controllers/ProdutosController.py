# from flask import jsonify,request
import os
import random
import json
import requests
import string

import sys
from flask import render_template, redirect, url_for, request, abort, session
from models.Tables import db, Produto

# from ln_oauth import auth, headers
def index():
    produtos = Produto.query.order_by(Produto.id).all()
    return render_template('produtos/index.html',produtos=produtos)
    return 'index'

def show(id):
    produto = Produto().query.filter_by(id=id).first()
    return render_template('produtos/form.html',produto=produto)
    return 'show'

def update(id):
    data = request.form
    produto = Produto.query.filter_by(id='id').update(
            nome=data['nome'],
            preco=data['preco'],
            preco_desconto=data['preco_desconto'],
            marca=data['marca'],
            modelo=data['modelo'],
            categoria=data['categoria'],
            ano=data['ano'],
            quantidade_estoque=data['quantidade'],
            descricao=data['descricao'],
            imagem=data['imagem'],
            ativo=('ativo' in data)
    )
    db.session.add(produto)
    db.session.commit()
    return redirect('/produtos')
    return 'update'

def create():
    produto = Produto()
    return render_template('produtos/form.html',produto=produto)

    return 'create'

def store():
    data = request.form
    produto = Produto(
            nome=data['nome'],
            preco=data['preco'],
            preco_desconto=data['preco_desconto'],
            marca=data['marca'],
            modelo=data['modelo'],
            ano= data['ano'],
            quantidade_estoque=data['quantidade'],
            descricao=data['descricao'],
            imagem=data['imagem'],
            ativo=('ativo' in data)
    )
    db.session.add(produto)
    db.session.commit()
    return redirect('/produtos')
    return 'store'

def destroy():
    produto = Produto().query.filter_by(id=id).first()
    db.session.delete(produto)
    db.session.commit()
    return redirect('/produtos')
    return 'destroy'