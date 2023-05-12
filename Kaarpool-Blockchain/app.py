import os
from flask import Flask, render_template, request
import utils.SQLiteDB as dbloader
from main import *

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


@app.route('/getDriverRouteData', methods=('GET', 'POST'))
def driverRouteData():
    if request.method == 'POST':
        driverRouteDataRequest = request.get_json()
        print(driverRouteDataRequest)
        driverRouteResponse = driverRouteGet(driverRouteDataRequest)
        print("driverRouteInfoResponse =", driverRouteResponse)
        if len(driverRouteResponse) > 0 and driverRouteResponse[0]["driverSlotStatus"] != "":
            slotStatus = False
        else:
            slotStatus = True
        return {"status": slotStatus, "data": driverRouteResponse}


@app.route('/getDriverRouteDataWithSrcAndDes', methods=('GET', 'POST'))
def driverRouteDataWithSrcDes():
    if request.method == 'POST':
        driverRouteDataRequest = request.get_json()
        print(driverRouteDataRequest)
        driverRouteResponse = driverRouteGetWithSrcDes(driverRouteDataRequest)
        print("driverRouteInfoResponse =", driverRouteResponse)
        if len(driverRouteResponse) > 0 and driverRouteResponse[0]["driverSlotStatus"] != "":
            slotStatus = False
        else:
            slotStatus = True
        return {"status": slotStatus, "data": driverRouteResponse}


@app.route('/getDriverRouteDataWithSrcDesAndTime', methods=('GET', 'POST'))
def driverRouteDataWithSrcDesTime():
    if request.method == 'POST':
        driverRouteDataRequest = request.get_json()
        print(driverRouteDataRequest)
        driverRouteResponse = driverRouteGetWithSrcDesTime(driverRouteDataRequest)
        print("Driver Route Info Response =", driverRouteResponse)
        if len(driverRouteResponse) > 0 and driverRouteResponse[0]["driverSlotStatus"] != "":
            # todo : slot status logic
            slotStatus = True
        else:
            slotStatus = True
        return {"status": slotStatus, "data": driverRouteResponse}
    # return render_template('riderRegister.html')


@app.route('/getRiderRouteData', methods=('GET', 'POST'))
def riderRouteData():
    if request.method == 'POST':
        riderRouteDataRequest = request.get_json()
        print("riderRouteDataRequest =", riderRouteDataRequest)
        riderRouteDataResponse = riderRouteGet(riderRouteDataRequest)
        print("riderRouteDataResponse =", riderRouteDataResponse)
        return {"status": True, "data": riderRouteDataResponse}


@app.route('/getRiderRouteDataWithName', methods=('GET', 'POST'))
def riderRouteDataWithNameSOurceDestination():
    if request.method == 'POST':
        riderRouteDataRequest = request.get_json()
        print("riderRouteDataRequest =", riderRouteDataRequest)
        riderRouteDataResponse = riderRouteGetWithNameSourceDestination(riderRouteDataRequest)
        print("riderRouteDataResponse =", riderRouteDataResponse)
        return {"status": True, "data": riderRouteDataResponse}


@app.route('/updateDriveRouteDataWithRiderName', methods=('GET', 'POST'))
def driveRouteDataWithRiderName():
    if request.method == 'POST':
        driveRouteDataRequestWithRiderName = request.get_json()
        print("driveRouteDataRequest for driveRouteDataRequestWithRiderName=", driveRouteDataRequestWithRiderName)
        driverRouteDataWithRiderNameResponse = updateDriveRouteWithRiderName(driveRouteDataRequestWithRiderName)
        print("driverRouteDataWithRiderNameResponse =", driverRouteDataWithRiderNameResponse)
        if driverRouteDataWithRiderNameResponse != None and driverRouteDataWithRiderNameResponse['rideSlotStatus'] == 0:
            slotStatus = False
        else:
            slotStatus = True
        return {"status": slotStatus, "data": driverRouteDataWithRiderNameResponse}
    # return render_template('riderRegister.html')


@app.route('/updateDriveRouteDataWithRiderStatus', methods=('GET', 'POST'))
def driveRouteDataWithRiderStatus():
    if request.method == 'POST':
        driveRouteDataRequestWithRiderName = request.get_json()
        print("driveRouteDataRequest for driveRouteDataRequestWithRiderName=", driveRouteDataRequestWithRiderName)
        driverRouteDataWithRiderNameResponse = updateDriveRouteWithRiderStatus(driveRouteDataRequestWithRiderName)
        print("driverRouteDataWithRiderNameResponse =", driverRouteDataWithRiderNameResponse)
        if driverRouteDataWithRiderNameResponse != None and driverRouteDataWithRiderNameResponse['rideSlotStatus'] == 0:
            slotStatus = False
        else:
            slotStatus = True
        return {"status": slotStatus, "data": driverRouteDataWithRiderNameResponse}


@app.route('/updateDriveRouteDataCancelRider', methods=('GET', 'POST'))
def driveRouteDataCancelRider():
    if request.method == 'POST':
        driveRouteDataRequestWithRiderName = request.get_json()
        print("driveRouteDataRequest for driveRouteDataRequestWithRiderName=", driveRouteDataRequestWithRiderName)
        driverRouteDataWithRiderNameResponse = updateDriveRouteCancelRider(driveRouteDataRequestWithRiderName)
        print("driverRouteDataWithRiderNameResponse =", driverRouteDataWithRiderNameResponse)
        if driverRouteDataWithRiderNameResponse != None and driverRouteDataWithRiderNameResponse['rideSlotStatus'] == 0:
            slotStatus = False
        else:
            slotStatus = True
        return {"status": slotStatus, "data": driverRouteDataWithRiderNameResponse}

@app.route('/startDriveRide', methods=('GET', 'POST'))
def driverRideStatus():
    if request.method == 'POST':
        driveRouteRideStatusRequest = request.get_json()
        print("driveRouteRideStatusRequest for driveRouteRideStatusRequest=", driveRouteRideStatusRequest)
        driverRouteRideStatusResponse = updateDriveRouteRideStatus(driveRouteRideStatusRequest)
        print("driverRouteRideStatusResponse =", driverRouteRideStatusResponse)
        return {"status": True, "data": driverRouteRideStatusResponse}\


@app.route('/endDriveRide', methods=('GET', 'POST'))
def driverRideStatusEnd():
    if request.method == 'POST':
        driveRouteRideStatusRequest = request.get_json()
        print("driveRouteRideStatusRequest for driveRouteRideStatusRequest=", driveRouteRideStatusRequest)
        driverRouteRideStatusResponse = updateDriveRouteRideStatusComplete(driveRouteRideStatusRequest)
        print("driverRouteRideStatusResponse =", driverRouteRideStatusResponse)
        return {"status": True, "data": driverRouteRideStatusResponse}
    # return render_template('riderRegister.html')


@app.route('/deleteDriveRouteDataWithRiderName', methods=('GET', 'POST'))
def deleteDriveRouteDataWithRiderName():
    if request.method == 'POST':
        driveRouteRideStatusRequest = request.get_json()
        print("driveRouteRideStatusRequest for driveRouteRideStatusRequest=", driveRouteRideStatusRequest)
        driverRouteRideStatusResponse = updateDriveRouteDeleteRiderName(driveRouteRideStatusRequest)
        print("driverRouteRideStatusResponse =", driverRouteRideStatusResponse)
        return {"status": True, "data": driverRouteRideStatusResponse}
    # return render_template('riderRegister.html')


@app.route('/getRiderBalance', methods=('GET', 'POST'))
def getRiderBalanceData():
    if request.method == 'POST':
        getBalanceDataRequest = request.get_json()
        print(getBalanceDataRequest)
        name = getBalanceDataRequest['name']
        riderBalance = print_eth_detail_rider()
        print("riderBalance =", riderBalance)
        return {"name": name, "balance": riderBalance}

@app.route('/getDriverBalance', methods=('GET', 'POST'))
def getDriverBalanceData():
    if request.method == 'POST':
        getBalanceDataRequest = request.get_json()
        print(getBalanceDataRequest)
        name = getBalanceDataRequest['name']
        driverBalance = print_eth_detail_driver()
        print("driverBalance =", driverBalance)
        return {"name": name, "balance": driverBalance}

# @app.route('/retrieveDriverData', methods=('GET', 'POST'))
# def retrieveDriverDataFromDB():
#     if request.method == 'POST':
#         getBalanceDataRequest = request.get_json()
#         print(getBalanceDataRequest)
#         name = getBalanceDataRequest['name']
#         riderBalance = retrieveDriverData()
#         print("riderBalance =", riderBalance)
#         return {"name": name, "balance": riderBalance}


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host='192.168.43.140')
