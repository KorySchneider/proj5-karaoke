import logging
import flask
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
