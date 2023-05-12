import utils.SQLiteDB as dbloader
from datetime import date

from main import send_eth_api


def driverRegistration(driverData):
    print(driverData)
    name = driverData['name']
    contactNo = driverData['contactNo']
    password = driverData['password']
    gender = driverData['gender']
    email = driverData['email']
    vehicle = driverData['vehicle']
    licenseNumber = driverData['licenseNumber']
    licenseValidity = driverData['licenseValidity']
    insuranceNumber = driverData['insuranceNumber']
    existingDriverData = dbloader.retrieveDriverDataWithLicenseNumber(licenseNumber)
    print("existingDriverData =", existingDriverData)
    if len(existingDriverData) < 1:
        dbloader.insertDriverData(name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity,
                                  insuranceNumber)
        print("Driver Registration Successful with name is", name)
        return {"name": name, "email": email, "message": "Driver Registration Successful", "status": True}
    else:
        print("Driver Email already exist with name is", name)
        return {"name": name, "email": email, "message": "Driver Email already exist", "status": False}


def riderRegistration(riderData):
    print(riderData)
    name = riderData['name']
    contactNo = riderData['contactNo']
    password = riderData['password']
    gender = riderData['gender']
    email = riderData['email']
    existingRiderData = dbloader.retrieveRiderDataWithEmail(email)
    print("existingRiderData =", existingRiderData)
    if len(existingRiderData) < 1:
        dbloader.insertRiderData(name, contactNo, password, gender, email)
        print("Rider Registration Successful with name is", name)
        return {"name": name, "email": email, "message": "Rider Registration Successful", "status": True}
    else:
        print("Rider Email already exist with name is", name)
        return {"name": name, "email": email, "message": "Rider Email already exist", "status": False}


def driverLoginToTable(driverLoginData):
    print(driverLoginData)
    # name = driverLoginData['name']
    email = driverLoginData['username']
    password = driverLoginData['password']
    driverData = dbloader.retrieveDriverDataWithEmailAndPassword(email, password)
    print("driverData =", driverData)
    if len(driverData) == 0:
        print("Driver Login Unsuccessful with email is", email)
        return {"name": None, "email": email,
                "message": "Invalid Credentials. Kindly use correct credentials", "status": False}
    else:
        print("Driver Login Successful with name is", driverData[0][1])
        return {"name": driverData[0][1], "email": email, "message": "Driver Login Successful", "status": True}


def riderLoginToTable(riderLoginData):
    print(riderLoginData)
    # name = riderLoginData['name']
    email = riderLoginData['username']
    password = riderLoginData['password']
    riderData = dbloader.retrieveRiderDataWithEmailAndPassword(email, password)
    print("riderData =", riderData)
    if len(riderData) == 0:
        return {"name": None, "email": email,
                "message": "Invalid Credentials. Kindly use correct credentials", "status": False}
    else:
        print("Rider Login Successful with name is", riderData[0][1])
        return {"name": riderData[0][1], "email": email, "message": "Rider Login Successful", "status": True}


def driverLoginValidation(name, pwd):
    driverData = dbloader.retrieveDriverDataWithNameAndPassword(name, pwd)
    print("driverData =", driverData)
    if len(driverData) == 0:
        return "Invalid Credentials. Kindly use correct credentials"
    else:
        print("Driver Login Successful with name is", name)
        return {"name": name, "email": driverData[0][5], "message": "Driver Login Successful", "status": True}


def riderLoginValidation(name, pwd):
    riderData = dbloader.retrieveRiderDataWithNameAndPassword(name, pwd)
    print("riderData =", riderData)
    if len(riderData) == 0:
        return "Invalid Credentials. Kindly use correct credentials"
    else:
        print("Rider Login Successful with name is", name)
        return {"name": name, "email": riderData[0][5], "message": "Rider Login Successful", "status": True}


def searchAllDriversWithRoutes(source, destination):
    drivers = dbloader.retrieveDriverRouteDataWithSourceAndDestination(source, destination)
    print("drivers =", drivers)
    return drivers


def driverRouteSet(driverRouteData):
    name = driverRouteData['name']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    availableSeats = driverRouteData['availableSeats']
    starttime = driverRouteData['starttime']
    currentTime = str(date.today()) + "_" + str(starttime)
    endtime = None
    dbloader.insertDriverRouteData(name, source, destination, availableSeats, currentTime, endtime)
    print("Driver Route Successfully Saved with name is", name)
    return {"name": name, "source": source, "destination": destination, "message": "Driver Route Successfully Saved",
            "status": True}


def riderRouteSet(riderRouteData):
    name = riderRouteData['name']
    source = riderRouteData['source']
    destination = riderRouteData['destination']
    time = riderRouteData['time']
    currentTime = str(date.today()) + "_" + str(time)
    dbloader.insertRiderRouteData(name, source, destination, currentTime)
    print("Driver Route Successfully Saved with name is", name)
    driversInfo = searchAllDriversWithRoutes(source, destination)
    print("driversInfo =", driversInfo)
    return driversInfo


def driverRouteGet(driverRouteData):
    name = driverRouteData['name']
    driverRouteDataWithName = dbloader.retrieveDriverRouteDataWithName(name)
    print("Driver Route Successfully Retrieve with name is", name)
    print("driverRouteDataWithName =", driverRouteDataWithName)
    return driverRouteDataWithName


def riderRouteGet(riderRouteData):
    source = riderRouteData['source']
    destination = riderRouteData['destination']
    riderRouteDataWithSourceAndDestination = dbloader.retrieveRiderRouteDataWithSourceAndDestination(source,
                                                                                                     destination)
    print("====== Rider Route Successfully Retrieve with Source {0} and Destination {1} ======".format(source, destination))
    print("riderRouteDataWithSourceAndDestination =", riderRouteDataWithSourceAndDestination)
    return riderRouteDataWithSourceAndDestination


def riderRouteGetWithNameSourceDestination(riderRouteData):
    name = riderRouteData['name']
    source = riderRouteData['source']
    destination = riderRouteData['destination']
    riderRouteDataWithName = dbloader.retrieveRiderRouteDataWithNameSourceDestination(name, source, destination)
    print("====== Rider Route Successfully Retrieve with Name {0} Source {1} Destination {2} ======".format(name, source, destination))
    print("riderRouteDataWithName =", riderRouteDataWithName)
    return riderRouteDataWithName


def driverRouteGetWithSrcDes(riderRouteData):
    source = riderRouteData['source']
    destination = riderRouteData['destination']
    driverRouteDataWithSourceAndDestination = dbloader.retrieveDriverRouteDataWithSourceAndDestination(source,
                                                                                                       destination)
    print("====== Rider Route Successfully Retrieve with Source {0} and Destination {1} ======".format(source, destination))
    print("====== driverRouteDataWithSourceAndDestination = ", driverRouteDataWithSourceAndDestination, "======")
    return driverRouteDataWithSourceAndDestination


def driverRouteGetWithSrcDesTime(riderRouteData):
    source = riderRouteData['source']
    destination = riderRouteData['destination']
    starttime = str(date.today()) + "_" + str(riderRouteData['starttime'])
    driverRouteDataWithSourceAndDestination = dbloader.retrieveDriverRouteDataWithSourceTimeAndDestination(source, destination, starttime)
    print("====== Rider Route Successfully Retrieve with Source {0} and Destination {1} ======".format(source, destination))
    print("====== driverRouteDataWithSourceAndDestination = ", driverRouteDataWithSourceAndDestination, "======")
    return driverRouteDataWithSourceAndDestination


def updateDriveRouteWithRiderName(driverRouteData):
    driveName = driverRouteData['driveName']
    riderName = driverRouteData['riderName']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    riderStatus = driverRouteData['riderStatus']
    time = str(date.today()) + "_" + str(driverRouteData['time'])
    driverRouteData = dbloader.retrieveDriverRouteDataWithDriverNameSourceDestinationAndTime(driveName, source, destination, time)
    if len(driverRouteData) > 0 and driverRouteData[0]["rider1"] != "" and driverRouteData[0]["rider2"] != "":
        return {"rideSlotStatus": 0, "info": "Sorry! Ride is full"}
    elif len(driverRouteData) > 0 and driverRouteData[0]["rider1"] == "":
        dbloader.updateDriverRouteDataWithRider1Name(driveName, source, destination, riderName, time, riderStatus)
    elif len(driverRouteData) > 0 and driverRouteData[0]["rider1"] != "" and driverRouteData[0]["rider2"] == "":
        dbloader.updateDriverRouteDataWithRider2Name(driveName, source, destination, riderName, time, riderStatus)
    dbloader.insertRiderRouteData(riderName, source, destination, time, 1, driveName)
    # dbloader.updateRiderRouteDataWithDriverName(driveName, source, destination, riderName, time)
    print("====== Driver Route Successfully Updated with Rider Name {0} ======".format(riderName))


def updateDriveRouteWithRiderStatus(driverRouteData):
    driveName = driverRouteData['driveName']
    riderName = driverRouteData['riderName']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    riderStatus = driverRouteData['riderStatus']
    time = str(date.today()) + "_" + str(driverRouteData['time'])

    driverRouteData = dbloader.retrieveDriverRouteDataWithDriverNameSourceDestinationAndTime(driveName, source, destination, time)
    if len(driverRouteData) > 0 and driverRouteData[0]["rider1"] == riderName:
        dbloader.updateDriverRouteDataWithRider1Status(driveName, source, destination, riderName, time, riderStatus)
    elif len(driverRouteData) > 0 and driverRouteData[0]["rider2"] == riderName:
        dbloader.updateDriverRouteDataWithRider2Status(driveName, source, destination, riderName, time, riderStatus)
    dbloader.insertRiderRouteData(riderName, source, destination, time, 1, driveName)
    # dbloader.updateRiderRouteDataWithDriverName(driveName, source, destination, riderName, time)
    print("====== Driver Route Successfully Updated with Rider Name {0} ======".format(riderName))


def updateDriveRouteCancelRider(driverRouteData):
    driveName = driverRouteData['driveName']
    riderName = driverRouteData['riderName']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    riderStatus = driverRouteData['riderStatus']
    time = str(date.today()) + "_" + str(driverRouteData['time'])

    driverRouteData = dbloader.retrieveDriverRouteDataWithDriverNameSourceDestinationAndTime(driveName, source, destination, time)
    if len(driverRouteData) > 0 and driverRouteData[0]["rider1"] == riderName:
        dbloader.updateDriverRouteDataCancelRider1(driveName, source, destination, riderName, time, riderStatus)
    elif len(driverRouteData) > 0 and driverRouteData[0]["rider2"] == riderName:
        dbloader.updateDriverRouteDataCancelRider2(driveName, source, destination, riderName, time, riderStatus)
    dbloader.deleteRiderRouteData(riderName, source, destination, time, driveName)
    # dbloader.updateRiderRouteDataWithDriverName(driveName, source, destination, riderName, time)
    print("====== Driver Route Successfully Updated with Cancel Rider Name {0} ======".format(riderName))


def updateDriveRouteRideStatus(driverRouteData):
    driveName = driverRouteData['driveName']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    time = driverRouteData['time']
    fareAmountInINR = driverRouteData['fare'].split(" ")[0]
    rideStatus = 1
    rider1Status = 1
    rider2Status = 1
    amountInETH = int(fareAmountInINR) * 0.000007272
    driverRouteData = dbloader.retrieveDriverRouteDataWithDriverNameSourceDestinationAndTime(driveName, source,
                                                                                             destination, time)

    if len(driverRouteData) > 0 and driverRouteData[0]["rider1"] != "" and driverRouteData[0]["rider2"] == "":
        dbloader.updateDriverRouteRideStatusRider1(driveName, source, destination, time, rideStatus, rider1Status)
    elif len(driverRouteData) > 0 and driverRouteData[0]["rider1"] != "" and driverRouteData[0]["rider2"] != "":
        dbloader.updateDriverRouteRideStatusRider2(driveName, source, destination, time, rideStatus, rider2Status)
    #dbloader.updateDriverRouteRideStatus(driveName, source, destination, time, rideStatus)
    print("=== Sending money to driver INR {0}  ETH {1}".format(fareAmountInINR, amountInETH))
    riderETHBalance, driverETHBalance = send_eth_api(amountInETH)
    print("====== Driver Route Status Changed Successfully =====")


def updateDriveRouteRideStatusComplete(driverRouteData):
    driveName = driverRouteData['driveName']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    time = driverRouteData['time']
    rideStatus = 2
    rider1Status = 3
    rider2Status = 3
    driverRouteData = dbloader.retrieveDriverRouteDataWithDriverNameSourceDestinationAndTime(driveName, source,
                                                                                             destination, time)
    if len(driverRouteData) > 0 and driverRouteData[0]["rider1"] != "" and driverRouteData[0]["rider2"] == "":
        dbloader.updateDriverRouteRideStatusRider1(driveName, source, destination, time, rideStatus, rider1Status)
    elif len(driverRouteData) > 0 and driverRouteData[0]["rider1"] != "" and driverRouteData[0]["rider2"] != "":
        dbloader.updateDriverRouteRideStatusRider2(driveName, source, destination, time, rideStatus, rider2Status)
    #dbloader.updateDriverRouteRideStatus(driveName, source, destination, time, rideStatus)
    dbloader.updateRiderRouteDataWithRideStatus(source, destination, time, rideStatus)
    print("====== Driver Route Status Changed Successfully =====")


def updateDriveRouteDeleteRiderName(driverRouteData):
    driverName = driverRouteData['driveName']
    source = driverRouteData['source']
    destination = driverRouteData['destination']
    riderName = driverRouteData['riderName']
    time = str(date.today()) + "_" + str(driverRouteData['time'])
    driverRouteResponse1 = dbloader.retrieveDriverRouteDataWithDriverNameRider1NameSourceDestinationAndTime(driverName, source, destination, time, riderName)
    if len(driverRouteResponse1):
        dbloader.updateDriverRouteDataWithRider1Name(driverName, source, destination, "", time, 0)
    driverRouteResponse2 = dbloader.retrieveDriverRouteDataWithDriverNameRider2NameSourceDestinationAndTime(driverName, source, destination, time, riderName)
    if len(driverRouteResponse2):
        dbloader.updateDriverRouteDataWithRider2Name(driverName, source, destination, "", time, 0)

    print("====== Driver Route Status Changed Successfully =====")

