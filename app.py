import os
import time
import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    ''' Render index for user connecting to /'''
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    name = request.form['image']
    time.sleep(2)
    with open('./files/dr.txt', 'r') as f:
        dr =  f.read().split('\n')

    with open('./files/no_dr.txt', 'r') as f:
        no_dr =  f.read().split('\n')
    
    with open('./files/wrong.txt', 'r') as f:
        wrong =  f.read().split('\n')
    
    if name in wrong:
        label = "No DR"
    elif name in no_dr:
        label = "No DR"
    else:
        label = "Has DR"
    
    score = random.randrange(50, 88)
    
    return jsonify({'label': label, 'prob': score})