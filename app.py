from classes.automation import Automation
from classes.employee import Employee

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    array_of_employees = []
    array_of_automations = []

    employeeDummy = {'Employee1': [30000,100],
                     'Employee2':[30000,100],
                     'Employee3':[30000,100],
                     'Employee4':[30000,100],
                     'Employee5':[30000,100],
                     'Employee6':[30000,100]
    }

    automationDummy = {'Automotan1' :(150)}

    tax_rate = 0.1

    #Populate array_of_employees
    for key,val in employeeDummy.items():
        array_of_employees.append(Employee(val[0],val[1]))
    #Populate array_of_automations
    for key,val in automationDummy.items():
        array_of_employees.append(Automation(val[0]))
################################################################################
    for emp in array_of_employees:
        print(Employee.salary)
    

    return render_template('index.html')

#@app.route('/',methods=['POST'])
#def main():
    # read the posted values from the UI
    # _name = request.form['inputName']
    # _email = request.form['inputEmail']
    # _password = request.form['inputPassword']

if __name__ == "__main__":
    app.run()
