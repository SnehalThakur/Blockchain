import utils.SQLiteDB as dbloader


def driverRegistration(driverData):
    print(driverData)
    name = driverData['name']
    contactNo = driverData['contactNo']
    password = driverData['password']
    gender = driverData['gender']
    email = driverData['vehicle']
    vehicle = driverData['email']
    licenseNumber = driverData['licenseNumber']
    licenseValidity = driverData['licenseValidity']
    dbloader.insertDriverData(name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity)
    print("Driver Registration Successful")
    return "Driver Registration Successful"


def riderRegistration(riderData):
    print(riderData)
    name = riderData['name']
    contactNo = riderData['contactNo']
    password = riderData['password']
    gender = riderData['gender']
    email = riderData['vehicle']
    dbloader.insertRiderData(name, contactNo, password, gender, email)
    print("Rider Registration Successful")
    return "Rider Registration Successful"


def driverLogin(driverLoginData):
    print(driverLoginData)
    name = driverLoginData['name']
    password = driverLoginData['password']
    driverData = dbloader.retrieveDriverDataWithNameAndPassword(name, password)
    if driverData.count() == 0:
        return "Invalid Credentials. Kindly use correct credentials"
    else:
        print("Driver Login Successful")
        return "Driver Login Successful"


def riderLogin(riderLoginData):
    print(riderLoginData)
    name = riderLoginData['name']
    password = riderLoginData['password']
    riderData = dbloader.retrieveRiderDataWithNameAndPassword(name, password)
    if riderData.count() == 0:
        return "Invalid Credentials. Kindly use correct credentials"
    else:
        print("Rider Login Successful")
        return "Rider Login Successful"


def driverLoginValidation(name, pwd):
    driverData = dbloader.retrieveDriverDataWithNameAndPassword(name, pwd)
    if driverData.count() == 0:
        return "Invalid Credentials. Kindly use correct credentials"
    else:
        print("Driver Login Successful")
        return "Driver Login Successful"


def riderLoginValidation(name, pwd):
    riderData = dbloader.retrieveRiderDataWithNameAndPassword(name, pwd)
    if riderData.count() == 0:
        return "Invalid Credentials. Kindly use correct credentials"
    else:
        print("Rider Login Successful")
        return "Rider Login Successful"


def searchAllDriversWithRoutes(source, destination):
    drivers = dbloader.retrieveDriverRouteDataWithSourceAndDestination(source, destination)
    return drivers
