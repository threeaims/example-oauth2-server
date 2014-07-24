# coding: utf-8

import requests
from flask import Flask, Response
from flask import session, request
from flask import render_template, redirect, jsonify

app = Flask(__name__, template_folder='templates')
app.debug = True
app.secret_key = 'secret3'
app.config.update({
    'SESSION_COOKIE_NAME': 'users',
})

@app.route('/')
def home():
    r = requests.get('http://127.0.0.1:5000/api/valid_token/' + request.headers['Authorization'][len('Bearer '):])
    if r.text == 'yes':
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='127.0.0.1', port=8001, debug=True)
   
