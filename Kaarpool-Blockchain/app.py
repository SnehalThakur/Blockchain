import os
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def deathStar():
    return render_template("1stpage.html")


@app.route('/riderLogin.html', methods=['GET', 'POST'])
def index():
    return render_template('riderLogin.html')


@app.route('/riderLogin', methods=['GET', 'POST'])
def riderLogin():
    if request.method == 'POST':
        result = request.form
        # return render_template("result.html", result=result)
        print(result)
        return result
    return render_template('riderLogin.html')


@app.route('/riderRegister.html', methods=('GET', 'POST'))
def about():
    return render_template('riderRegister.html')


@app.route('/riderRegister', methods=('GET', 'POST'))
def riderRegister():
    if request.method == 'POST':
        result = request.form
        # return render_template("result.html", result=result)
        print(result)
        return result
    return render_template('riderRegister.html')


@app.route('/driverLogin.html', methods=('GET', 'POST'))
def menu():
    return render_template('driverLogin.html')


@app.route('/driverRegister.html', methods=('GET', 'POST'))
def contact():
    return render_template('driverRegister.html')


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
