from classes.automation import Automation
from classes.employee import Employee

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    employee = Employee('salary', 12000.00, 0.00, 25.00, 1000.00, 15000.00)
    employee = Employee('hourly', 12.00, 550, 25.00, 1000.00, 15000.00)
    employee = Automation(600, 50.00, .005, 15000.00)
    return render_template('index.html')

#@app.route('/',methods=['POST'])
#def main():
    # read the posted values from the UI
    # _name = request.form['inputName']
    # _email = request.form['inputEmail']
    # _password = request.form['inputPassword']

if __name__ == "__main__":
    app.run()
