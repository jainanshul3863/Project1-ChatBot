from flask import Flask, render_template, request, redirect
from dataload import loadData
import os

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('reqpage.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        file = request.files['data']
        file.save(file.filename)
        loadData(file.filename)
        q = 'python Backend/dynamictrain.py ' + file.filename
        os.system(q)
        os.system('python Backend/train.py')

    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)
