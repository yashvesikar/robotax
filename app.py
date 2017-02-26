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
    print(data)
    array_of_employees = []
    array_of_automations = []

    for key,value in data.items():
        value = value[:-1]
        if key == 'oldEmployees':
            for employee in value:
                array_of_employees.append(Employee(employee['averageTax'],\
                                                   employee['wage'],\
                                                   employee['productivity'],\
                                                   employee['numberOfEmployees'],\
                                                   False))

        if key == 'newEmployees':
            for employee in value:
                array_of_employees.append(Employee(employee['averageTax'],\
                                                   employee['wage'],\
                                                   0,\
                                                   employee['numberOfEmployees'],\
                                                   True))
        if key == 'automations':
            for automation in value:
                array_of_automations.append(Automation(automation['productivity'],\
                                                       automation['cost'],\
                                                       automation['numberOfAutomations'],\
                                                       automation['lifeSpan']))


    #Employee data
    total_tax = sum(emp.Tax()*emp.NumberOfEmployees() for emp in array_of_employees if emp.Status() == False)
    total_salary = sum(emp.Wage()*emp.NumberOfEmployees() for emp in array_of_employees if emp.Status() == False)
    total_production = sum(emp.Production()*emp.NumberOfEmployees() for emp in array_of_employees if emp.Status() == False)

    #Left hand side of equation, employee side
    lhs = (total_tax) / total_production

    #Robot data
    robots_added = len(array_of_automations) #This is incorrect
    robots_production = sum(automation.Production()*automation.NumberOfAutomations() for automation in array_of_automations)
    #Technician data/new employee data
    technicians_tax = sum(emp.Tax()*emp.NumberOfEmployees() for emp in array_of_employees if emp.Status() == True)
    technicians_salary = sum(emp.Wage()*emp.NumberOfEmployees() for emp in array_of_employees if emp.Status() == True)

    robot_tax = (lhs*robots_production) - technicians_tax

    oldest_robot = 0
    for robot in array_of_automations:
        if robot.LifeSpan() > oldest_robot:
            oldest_robot = robot.LifeSpan()
    robots_cost = sum(robot.Cost() / robot.LifeSpan() for robot in array_of_automations)
    robots_cost += robot_tax
    robots_cost += technicians_tax + technicians_salary

    return str([robot_tax, robot_tax+technicians_tax-total_tax, robots_cost*oldest_robot, total_salary*oldest_robot, oldest_robot])
    # read the posted values from the UI
    # _name = request.form['inputName']
    # _email = request.form['inputEmail']
    # _password = request.form['inputPassword']

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
