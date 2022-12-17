import SQLiteDB as dbloader


def driverLoginValidation(name, pwd):
    driverData = dbloader.retrieveDriverDataWithNameAndPassword(name, pwd)
    if driverData.count() == 0:
        return "Invalid Credentials. Kindly use correct credentials"


def riderLoginValidation(name, pwd):
    riderData = dbloader.retrieveRiderDataWithNameAndPassword(name, pwd)
    if riderData.count() == 0:
        return "Invalid Credentials. Kindly use correct credentials"


def searchAllDriversWithRoutes(source,destination):
    drivers = dbloader.retrieveDriverRouteDataWithSourceAndDestination(source, destination)
    return drivers