from classes.automation import Automation
from classes.employee import Employee
import json
import ast

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    tax_rate = 0.1
    return render_template('index.html')



@app.route('/calculations',methods=['POST'])
def calculations():

    data = ast.literal_eval(request.form.to_dict().keys()[0])

    array_of_employees = []
    array_of_automations = []

    for key,value in data.items():
        value = value[:-1]
        if key == 'oldEmployees':
            for employee in value:
                array_of_employees.append(Employee(employee['averageTax'],\
                                                   employee['wage'],\
                                                   employee['productivity'],\
                                                   False))

        if key == 'newEmployees':
            for employee in value:
                array_of_employees.append(Employee(employee['averageTax'],\
                                                   employee['wage'],\
                                                   0,\
                                                   True))
        if key == 'automations':
            for automation in value:
                array_of_automations.append(Automation(automation['productivity'],\
                                                       automation['cost']))



    #Employee data
    total_tax = sum(emp.Tax() for emp in array_of_employees if emp.Status() == False)
    total_production = sum(emp.Production() for emp in array_of_employees if emp.Status() == False)

    #Left hand side of equation, employee side
    lhs = (total_tax) / total_production

    #Robot data
    robots_added = len(array_of_automations)
    robots_production = sum(automation.Production() for automation in array_of_automations)
    #Technician data/new employee data
    technicians_tax = sum(emp.Tax() for emp in array_of_employees if emp.Status() == True)


    robot_tax = (lhs*robots_production) - technicians_tax

    increase = robot_tax - total_tax;

    return str([robot_tax, increase])


@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
