import classes

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

#@app.route('/',methods=['POST'])
#def main():
    # read the posted values from the UI
    # _name = request.form['inputName']
    # _email = request.form['inputEmail']
    # _password = request.form['inputPassword']

if __name__ == "__main__":
    app.run()
