oAuth
+++++

Tips
====

* Use 127.0.0.1 everywhere, not localhost
* `api/me` only works with an oauth bearer token in the Authorization

Background
==========

A platform (whatever shape it takes) will need the following:

* Workflow engine
* Single Sign on
* Authorization token
* User management
* Application Client Management

The code in this directory is a proof of concept for:

`auth.py`:

* Sign in
* User store
* Application Client store

`service.py`:

* Sample Service

`client.py`:

* Sample client

The user will login via the client which will redirect to the auth server to
sign in. Once sign in is complete, the client will be able to access the
service on behalf of the user.


* Authorize

Install
=======

~~~
virtualenv env
. env/bin/activate
pip install -r requirements.txt
cd flask-oauthlib
python setup.py develop
~~~

OAUTHLIB_INSECURE_TRANSPORT

* http://lepture.com/en/2013/create-oauth-server
* https://github.com/lepture/example-oauth2-server
* http://flask-oauthlib.readthedocs.org/en/latest/oauth2.html

Setup
=====

Run:

~~~
python app.py
~~~

Visit http://localhost:5000 and login with a username. This will create the user. Now visit http://localhost:5000/client and a client will be created with the credentials returned.

Now add the credentials to `client.py` and run the client:

~~~
python client.py
~~~

Visit http://localhost:8000

You'll be redirected to `app.py` where since you are signed in you'll be shown the ID of the client trying to register, and asked to grant access. If you choose no you get an attribute error. If you choose yes you get shown an oauth token.

Now you can access http://localhost:8000 and see your username or go to /authorized to see your access token.

Now we want to access a third serivce.

We can go to http://localhost:5000/api/me and you should see your username, but you don't currently. We don't have the correct headers.

