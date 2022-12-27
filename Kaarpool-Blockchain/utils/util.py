import utils.SQLiteDB as dbloader
from datetime import date

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
    currentTime = date.today()+ "_"+starttime
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
    currentTime = date.today() + "_" + time
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
    riderRouteDataWithSourceAndDestination = dbloader.retrieveRiderRouteDataWithSourceAndDestination(source, destination)
    print("Rider Route Successfully Retrieve with Source {0} and Destination {1}".format(source, destination))
    print("riderRouteDataWithSourceAndDestination =", riderRouteDataWithSourceAndDestination)
    return riderRouteDataWithSourceAndDestination


