"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, g
from flask import request
from NL2SQL import app
import json
from flask import jsonify
from DBTasks import DBTasks
import os
import sys

@app.before_request
def connect_db() :
    g.db = DBTasks()

    auth = open("./DBConfig.txt", "r")
    secret_lines = auth.readlines()
    secret_data = None
    for secret_line in secret_lines :
        if secret_line[0] == '#':
            continue
        else :
            secret_line = secret_line.rstrip()
            secret_data = secret_line.split(",")
    g.db.configDB(secret_data[0], secret_data[1], secret_data[2], secret_data[3])

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )


# Make application access data
@app.route('/getSQLQueryData', methods=['GET', 'POST'])
def fetchData():
    NL_sentence = request.args.get('NL_sentence')
    print('Received call from client with argument Sentence: ' + NL_sentence)
    SQL_query = g.db.fetchDataFromDB(NL_sentence)
    
    print('Sending Data: ' + SQL_query)
    return json.dumps(SQL_query)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
