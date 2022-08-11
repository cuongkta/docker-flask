from app import app
from flask import Flask, request, jsonify


@app.route('/')
def home():
   return "hello world!"


@app.route('/hello2/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})
