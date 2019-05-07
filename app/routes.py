from flask import *
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/showdata',methods=['GET','POST'])
def show_data():
    userdata = dict(request.form)
    print(userdata)
    return render_template('showdata.html', name=userdata['name'][0], age=userdata['age'][0])
