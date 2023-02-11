# from flask import jsonify,request
import os
import random
import json
import requests
import string
import datetime
import sys
from flask import render_template, redirect, url_for, request, abort, session
from models.Tables import db, User, Carteira, UserConquista, CarteiraHistorico
from dotenv import load_dotenv

project_folder = os.path.expanduser(os.path.dirname(os.path.abspath(__file__)))  # adjust as appropriate

load_dotenv(os.path.join(project_folder, '.flaskenv'))


# from ln_oauth import auth, headers


def user_info(api_url,client_id,client_secret,redirect_uri,code):
    '''
    Get user information from Linkedin
    '''
    params = {
        'grant_type':'authorization_code',
        # 'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'code': code,
        'client_secret': client_secret
        # 'scope': 'r_liteprofile,r_emailaddress,w_member_social'
        }
    response = requests.post(f'{api_url}/accessToken',params=params)
    token = response.json()['access_token']
    # user_info = response.json()
    headers = {'Authorization': 'Bearer '+token,
    'cache-control': 'no-cache',
    'X-Restli-Protocol-Version': '2.0.0'}
    response = requests.get('https://api.linkedin.com/v2/me', headers = headers)
    user_info = response.json()
    return user_info

def create_CSRF_token():
    '''
    This function generates a random string of letters.
    It is not required by the Linkedin API to use a CSRF token.
    However, it is recommended to protect against cross-site request forgery
    '''
    letters = string.ascii_lowercase
    token = ''.join(random.choice(letters) for i in range(20))
    return token

def open_url(url):
    '''
    Function to Open URL.
    Used to open the authorization link
    '''
    import webbrowser
    print(url)
    webbrowser.open(url)

def parse_redirect_uri(redirect_response):
    '''
    Parse redirect response into components.
    Extract the authorized token from the redirect uri.
    '''
    from urllib.parse import urlparse, parse_qs
 
    url = urlparse(redirect_response)
    url = parse_qs(url.query)
    return url['code'][0]

def authorize(api_url,client_id,client_secret,redirect_uri):
    '''
    Make a HTTP request to the authorization URL.
    It will open the authentication URL.
    Once authorized, it'll redirect to the redirect URI given.
    The page will look like an error. but it is not.
    You'll need to copy the redirected URL.
    '''
    # Request authentication URL
    csrf_token = create_CSRF_token()
    params = {
        'response_type': 'code',
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        # 'state': csrf_token,
        'scope': 'r_liteprofile,r_emailaddress,w_member_social'
        }
 
    response = requests.get(f'{api_url}/authorization',params=params)
        url = f"{api_url}/authorization?response_type=code&scope=r_liteprofile,r_eme,r_emailaddress,w_member_social&client_id={client_id}&redirect_uri={redirect_uri}"
    print(f'''
    The Browser will open to ask you to authorize the credentials.\n
    Since we have not set up a server, you will get the error:\n
    This site can’t be reached. localhost refused to connect.\n
    This is normal.\n
    You need to copy the URL where you are being redirected to.\n
    ''')
 
    open_url(url)
 
    # Get the authorization verifier code from the callback url
    #redirect_response = input('Paste the full redirect URL here:')
    #auth_code = parse_redirect_uri(redirect_response)
    return url

def jogo():

    return render_template('usuario.html') 
    return session['auth']


def Linkedin_call():# creds = read_creds('credentials.json')
    # return "hello"
    data = request.args
    if(data):
        client_id, client_secret = os.environ.get("CLIENT_ID"), os.environ.get("CLIENTE_SECRET")
        redirect_uri = os.environ.get("REDIRECT_URI")
        api_url = 'https://www.linkedin.com/oauth/v2'
        # return(redirect_uri)
        info = user_info(api_url,client_id,client_secret,redirect_uri,data['code'])
        user_db = User.query.filter_by(linkedin_id=info['id']).first()
        carteira_db = Carteira.query.filter_by(user_id=user_db.id).first()
        if user_db is None:
            user_db = User(nome=(info['localizedFirstName']+' '+info['localizedLastName'] ), 
                        linkedin_id=info['id'],avatar=info['profilePicture']['displayImage'])
            db.session.add(user_db)
            db.session.commit()
            carteira_db = Carteira(user_id=user_db.id,moedas=5,conquistas=1)
            user_conquista_db = UserConquista(user_id=user_db.id,conquista_id=1,created_at=datetime.datetime.now())
            db.session.add(carteira_db)
            db.session.add(user_conquista_db)
            db.session.commit()
            historico = CarteiraHistorico(carteira_id=carteira_db.id,moedas=5,evento='Primeiro Login',created_at=datetime.datetime.now())
            db.session.add(historico)
            db.session.commit()
        carteira_db = Carteira.query.filter_by(user_id=user_db.id).first()
        session['user'] = {}
        session['user']['id'] = user_db.id
        session['user']['linkedin_id'] = user_db.linkedin_id
        session['user']['nome'] = user_db.nome
        session['user']['avatar'] = user_db.avatar
        session['user']['moedas'] = carteira_db.moedas
        return redirect('/desafios/painel')

    else:
        return render_template('login.html') 
    return jsonify(
        username='teste a',
        email='teste b',
        id='teste x'
    )

def login_linkedin():# creds = read_creds('credentials.json')
    client_id, client_secret = os.environ.get("CLIENT_ID"), os.environ.get("CLIENTE_SECRET")
    redirect_uri = os.environ.get("REDIRECT_URI")
    api_url = 'https://www.linkedin.com/oauth/v2'
    # return(redirect_uri)
    return redirect(authorize(api_url,client_id,client_secret,redirect_uri))
    # return "hello"
    return jsonify(
        username='teste a',
        email='teste b',
        id='teste x'
    )