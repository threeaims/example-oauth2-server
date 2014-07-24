from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os

app = Flask(__name__)
app.debug = True
app.secret_key = 'secret2'
app.config.update({
    'SESSION_COOKIE_NAME': 'client2',
})

from client import CLIENT_ID, CLIENT_SECRET

authorization_base_url = 'http://127.0.0.1:5000/oauth/authorize'
token_url = 'http://127.0.0.1:5000/oauth/token'

@app.route("/")
def demo():
    remote = OAuth2Session(CLIENT_ID, scope=['email'])
    authorization_url, state = remote.authorization_url(authorization_base_url)
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route("/authorized", methods=["GET"])
def authorized(): # this is where it fails
    print "+++++++++++++"
    print session
    print request
    print request.headers
    remote = OAuth2Session(CLIENT_ID, scope=['email'], state=session['oauth_state'])
    token = remote.fetch_token(token_url, client_secret=CLIENT_SECRET, authorization_response=request.url, method=u'GET')
    session['access_token'] = token
    return redirect(url_for('.profile'))

@app.route("/profile", methods=["GET"])
def profile():
    remote = OAuth2Session(CLIENT_ID, token=session['access_token'])
    return jsonify(remote.get('http://127.0.0.1:5000/api/me').json())

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    import os
    os.environ['DEBUG'] = 'true'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
    app.run(host='127.0.0.1', port=8000, debug=True)

