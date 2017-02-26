from classes.automation import Automation
from classes.employee import Employee

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():

    TAX_RATE = 0.1
    
    # 0 - number
    # 1 - tax rate
    # 2 - wage
    # 3 - productivity
    
    _old_employees = []
    _new_employees = []
    _new_automations = []
        
    
    # Fired Employee data
    #old_salary = sum(employee[0] * employee[2] for employee in _old_employees)
    #old_salary_tax = get_taxes(location, _old_employees)
    old_tax = sum(employee[0] * employee[1] for employee in _old_employees)
    old_production = sum(employee[0] * employee[3] for employee in _old_employees)

    # New Hire data
    #tech_salary = sum(employee[0] * employee[2] for employee in _new_employees)
    #tech_salary_tax = get_taxes(location, _new_employees)
    tech_tax = sum(employee[0] * employee[1] for employee in _new_employees)
    
    # Robot Production
    new_production = sum(robot[0] * robot[3] for robot in _new_automations)
    
    # Production ratio
    prod_ratio = new_production / old_production
    
    robot_tax = old_production * prod_ratio - technicians_tax

    print("Robot Tax: ", robot_tax)
    print("Per robot tax: ", robot_tax / len(_new_automations))

    return render_template('index.html')

#@app.route('/',methods=['POST'])
#def main():
    # read the posted values from the UI
    # _name = request.form['inputName']
    # _email = request.form['inputEmail']
    # _password = request.form['inputPassword']

if __name__ == "__main__":
    app.run()
