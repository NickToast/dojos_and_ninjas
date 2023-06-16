from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.dojos_model import Dojo
from flask_app.models import ninjas_model

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)


#ACTION PAGE FOR ADDING A NEW DOJO, DO NOT RENDER TEMPLATE
@app.route('/dojos/add', methods=['POST'])
def add_dojo():
    Dojo.save(request.form)
    return redirect ('/dojos')


@app.route('/dojos/<int:dojos_id>')
def show(dojos_id):
    dojo = Dojo.get_dojo_with_ninjas({"id": dojos_id})
    for ninja in dojo.ninjas:
        print(ninja.name)
    return render_template('dojo_show.html', dojo=dojo)

