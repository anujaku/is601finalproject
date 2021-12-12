import csv

from pandas import read_csv

from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Please enter numeric values in both fields and try again.'
            return render_template('calculator.html', error=error)

            #return render_template('calculator.html', error=error)
         #elif request.form['value1'] == '/[^a-zA-Z0-9 ]/g' or request.form['value2'] == '[/a-zA-Z/]':
             #error = 'Please enter numeric values'
             #return render_template('calculator.html', error=error)
        else:
            flash('Calculation is successful.Please find result below.')

            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_calculation_from_result())

            fieldnames = ['value1', 'value2', 'operation', 'result']
            with open('output.csv', 'a', newline='') as inFile:
                writer = csv.DictWriter(inFile, fieldnames=fieldnames)
                writer.writerow({'value1': value1, 'value2': value2,
                                 'operation': operation, 'result': result})
            inFile.close()
            df = read_csv('output.csv')
            data = df.values
            return render_template('result.html', data=data)

            #return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)

    @staticmethod
    def get():
        return render_template('calculator.html')