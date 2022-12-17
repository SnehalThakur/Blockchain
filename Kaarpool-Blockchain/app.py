import os
from flask import Flask, render_template, request
import utils.SQLiteDB as dbloader

# Configure application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def startPage():
    return render_template("1stpage.html")


# @app.route('/riderLogin.html', methods=['GET', 'POST'])
# def index():
#     return render_template('riderLogin.html')


@app.route('/riderLogin', methods=['GET', 'POST'])
def riderLogin():
    if request.method == 'POST':
        result = request.form
        print(result)
        return result
    return render_template('riderLogin.html')


# @app.route('/riderRegister.html', methods=('GET', 'POST'))
# def about():
#     return render_template('riderRegister.html')


@app.route('/riderRegister', methods=('GET', 'POST'))
def riderRegister():
    if request.method == 'POST':
        result = request.form
        print(result)
        return result
    return render_template('riderRegister.html')


@app.route('/driverLogin', methods=('GET', 'POST'))
def driverLogin():
    return render_template('driverLogin.html')


@app.route('/driverRegister', methods=('GET', 'POST'))
def driverRegister():
    return render_template('driverRegister.html')


@app.route('/driverRoute', methods=('GET', 'POST'))
def driverRoute():
    if request.method == 'POST':
        result = request.form
        print(result)
        return result
    return render_template('riderRegister.html')


@app.route('/riderRoute', methods=('GET', 'POST'))
def riderRoute():
    if request.method == 'POST':
        result = request.form
        print(result)
        return result
    return render_template('riderRegister.html')


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
