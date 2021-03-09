"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from BMIproject import app 
import BMIproject.calculation as calc

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Home',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='If you have any questions send e-mail.'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title='About application',
        year=datetime.now().year,
    )

@app.route('/calculate', methods=['post', 'get'])
def calculate():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        sex = request.form.get('sex')
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')

        if name == '':
            message = 'Name is incorrect!'
        elif sex != 'men' and sex != 'women':
            message = 'You didnt choose sex!'
        elif age == '':
            message = 'Age is incorrect'
        elif height == '':
            message = 'Height is incorrect'
        elif weight == '':
            message = 'Weight is incorrect'
        else:
            return redirect(url_for('result', name = name, sex=sex, age=age, height=height, weight=weight))

    return render_template(
        'calculate.html',
        title='Calculation',
        year=datetime.now().year,
        error = message
    )

@app.route('/result')
def result():
    name = request.args.get('name', None)
    sex =  request.args.get('sex', None)
    age =  request.args.get('age', None)
    height = request.args.get('height', None)
    weight = request.args.get('weight', None)

    cal = calc.BMI(sex,age,height,weight)

    calMiffinStJeor = str(cal.calculateMiffin())
    calHarrrisBenedicta = str(cal.calculateHarris())
    BMI = str(cal.bmi())
    category = str(cal.category())


    return render_template(
        'result.html',
        title='Result',
        year=datetime.now().year,
        BMI = BMI,
        calMiffinStJeor = calMiffinStJeor,
        calHarrrisBenedicta = calHarrrisBenedicta,
        name = name,
        category = category
    )