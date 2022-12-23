import os
from flask import Flask, render_template, request
import utils.SQLiteDB as dbloader

# Configure application
from utils.util import *

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def startPage():
    return render_template("1stpage.html")

@app.route("/riderHomePage")
def riderPage():
    return render_template("riderPage.html")

@app.route("/driverHomePage")
def driverPage():
    return render_template("driverPage.html")

# @app.route('/riderLogin.html', methods=['GET', 'POST'])
# def index():
#     return render_template('riderLogin.html')

@app.route('/riderLogin', methods=['GET', 'POST'])
def riderLogin():
    if request.method == 'POST':
        riderLoginData = request.get_json()
        print(riderLoginData)
        riderLoginResponse = riderLoginToTable(riderLoginData)
        print("riderLoginResponse =", riderLoginResponse)
        return riderLoginResponse
    return render_template('riderLogin.html')


# @app.route('/riderRegister.html', methods=('GET', 'POST'))
# def about():
#     return render_template('riderRegister.html')


@app.route('/riderRegister', methods=('GET', 'POST'))
def riderRegister():
    if request.method == 'POST':
        riderData = request.get_json()
        print("riderData=", riderData)
        riderRegistrationResponse = riderRegistration(riderData)
        print("riderRegistrationResponse =", riderRegistrationResponse)
        return riderRegistrationResponse
    return render_template('riderRegister.html')


@app.route('/driverLogin', methods=('GET', 'POST'))
def driverLogin():
    if request.method == 'POST':
        driverLoginData = request.get_json()
        print(driverLoginData)
        driverLoginResponse = driverLoginToTable(driverLoginData)
        print("driverLoginResponse =", driverLoginResponse)
        return driverLoginResponse
    return render_template('driverLogin.html')


@app.route('/driverRegister', methods=('GET', 'POST'))
def driverRegister():
    if request.method == 'POST':
        driverData = request.get_json()
        print("driverData= ", driverData)
        driverRegistrationResponse = driverRegistration(driverData)
        print("driverRegistrationResponse =", driverRegistrationResponse)
        return driverRegistrationResponse
    return render_template('driverRegister.html')


@app.route('/driverRoute', methods=('GET', 'POST'))
def driverRoute():
    if request.method == 'POST':
        driverRouteData = request.get_json()
        print(driverRouteData)
        driverRouteInfo = driverRouteSet(driverRouteData)
        print("driverRouteInfoResponse =", driverRouteInfo)
        return driverRouteInfo
    return render_template('riderRegister.html')


@app.route('/riderRoute', methods=('GET', 'POST'))
def riderRoute():
    if request.method == 'POST':
        riderRouteData = request.get_json()
        print("riderRouteData =", riderRouteData)
        driversInfo = riderRouteSet(riderRouteData)
        print("driversInfoResponse =", driversInfo)
        return driversInfo
    return render_template('riderRegister.html')


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
