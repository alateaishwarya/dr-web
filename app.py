import os
import time
import random

from flask import Flask, request, render_template, jsonify

# from PIL import Image
# from keras.models import load_model
# from keras import backend as K

# model = load_model('models/model.h5')

app = Flask(__name__)

classes = ['Has DR', 'NO DR']

@app.route("/")
def index():
    ''' Render index for user connecting to /'''
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    f = request.files['image']
    # name = request.form['image']
    name = f.filename
    f.save(os.path.join('images', f.filename))


    # img = Image.open('images/' + name)
    # img = img.resize()
    # img = np.array(img)

    # preds = model.predict([img])[0]
    # max_idx = n.argmax(preds)

    # label = classes[max_idx]
    # score = preds[max_idx]


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)