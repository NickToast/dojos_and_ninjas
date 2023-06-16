from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo

@app.route('/ninjas')
def ninja_index():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos = dojos)

#SHOW ROUTE FOR NINJAS
@app.route('/ninjas')
def show_add_ninja():
    all_dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos = all_dojos)

#ACTION ROUTE FOR ADD NINJA FORM
@app.route('/ninjas/add', methods=['POST'])
def add_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }

    Ninja.add_ninja(data)

    return redirect ('/')
    #change this redirect to the dojo show page when working

