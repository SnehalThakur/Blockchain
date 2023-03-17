import sqlite3 as sql


def createRiderTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS rider (
                            id integer primary key autoincrement,
                            name text not null,
                            contactNo text not null,
                            password text not null,
                            gender text not null,
                            email text not null,
                            balance integer
                        );
                    """)


def createDriverTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS driver (
                            id integer primary key autoincrement,
                            name text not null,
                            contactNo text not null,
                            password text not null,
                            gender text not null,
                            email text not null,
                            vehicle text not null,
                            licenseNumber text not null,
                            licenseValidity integer not null,
                            insuranceNumber integer not null,
                            balance integer
                        );
                    """)


def createRiderRouteTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS riderRoute (
                            id integer primary key autoincrement,
                            name text not null,
                            source text not null,
                            destination text not null,
                            time text not null,
                            confirmRideStatus integer,
                            driverName text
                        );
                    """)


def createDriverRouteTableIfNotExist():
    sqlConnection = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS driverRoute (
                            id integer primary key autoincrement,
                            name text not null,
                            source text not null,
                            destination text not null,
                            availableSeats integer not null,
                            starttime text not null,
                            endtime text,
                            rider1 text,
                            rideStatus integer,
                            rider2 text
                        );
                    """)


# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())

def insertDriverData(name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity, insuranceNumber):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()

    cur.execute(
        "INSERT INTO driver (name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity, insuranceNumber) VALUES (?,?,?,?,?,?,?,?,?)",
        (name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity, insuranceNumber))
    con.commit()
    con.close()


def insertRiderData(name, contactNo, password, gender, email):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO rider (name, contactNo, password, gender, email) VALUES (?,?,?,?,?)",
                (name, contactNo, password, gender, email))
    con.commit()
    con.close()


def insertDriverRouteData(name, source, destination, availableSeats, starttime, endtime):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO driverRoute (name, source, destination, availableSeats, starttime, endtime, rider1, rideStatus, rider2) VALUES (?,?,?,?,?,?,?,?,?)",
        (name, source, destination, availableSeats, starttime, endtime, "", "0", ""))
    con.commit()
    con.close()


def insertRiderRouteData(name, source, destination, time, confirmRideStatus, driverName):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO riderRoute (name, source, destination, time, confirmRideStatus, driverName) VALUES (?,?,?,?,?,?)",
                (name, source, destination, time, confirmRideStatus, driverName))
    con.commit()
    con.close()


def retrieveDriverData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM driver")
    driverData = cur.fetchall()
    driverData_accumulator = []
    for item in driverData:
        driverDataDict = {}
        driverDataDict["id"] = item[0]
        driverDataDict["name"] = item[1]
        driverDataDict["contactNo"] = item[2]
        driverDataDict["password"] = item[3]
        driverDataDict["gender"] = item[4]
        driverDataDict["email"] = item[5]
        driverDataDict["vehicle"] = item[6]
        driverDataDict["licenseNumber"] = item[7]
        driverDataDict["licenseValidity"] = item[8]
        driverDataDict["insuranceNumber"] = item[9]
        driverDataDict["balance"] = item[10]
        driverData_accumulator.append(driverDataDict)
    print("driverData =", driverData_accumulator)
    con.close()
    return driverData_accumulator


def retrieveRiderData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM rider")
    riderData = cur.fetchall()
    riderRouteData_accumulator = []
    for item in riderData:
        riderDataDict = {}
        riderDataDict["id"] = item[0]
        riderDataDict["name"] = item[1]
        riderDataDict["contactNo"] = item[2]
        riderDataDict["password"] = item[3]
        riderDataDict["gender"] = item[4]
        riderDataDict["email"] = item[5]
        riderDataDict["balance"] = item[6]
        riderRouteData_accumulator.append(riderDataDict)
    print("riderData =", riderRouteData_accumulator)
    con.close()
    return riderRouteData_accumulator


def retrieveDriverRouteData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM driverRoute")
    driverRouteData = cur.fetchall()
    driverRouteData_accumulator = []
    for item in driverRouteData:
        driverDataDict = {}
        driverDataDict["id"] = item[0]
        driverDataDict["name"] = item[1]
        driverDataDict["source"] = item[2]
        driverDataDict["destination"] = item[3]
        driverDataDict["availableSeats"] = item[4]
        driverDataDict["starttime"] = item[5]
        driverDataDict["endtime"] = item[6]
        driverDataDict["rider1"] = item[7]
        driverDataDict["rideStatus"] = item[8]
        driverDataDict["rider2"] = item[9]
        driverRouteData_accumulator.append(driverDataDict)
    print("driverRouteData =", driverRouteData_accumulator)
    con.close()
    return driverRouteData_accumulator



def retrieveRiderRouteData():
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM riderRoute")
    riderRouteData = cur.fetchall()
    riderRouteData_accumulator = []
    for item in riderRouteData:
        riderRouteDataDict = {}
        print("item.keys() =", item[0])
        riderRouteDataDict["id"] = item[0]
        riderRouteDataDict["name"] = item[1]
        riderRouteDataDict["source"] = item[2]
        riderRouteDataDict["destination"] = item[3]
        riderRouteDataDict["time"] = item[4]
        riderRouteDataDict["confirmRideStatus"] = item[5]
        riderRouteDataDict["driverName"] = item[6]
        riderRouteData_accumulator.append(riderRouteDataDict)
    print("riderRouteData =", riderRouteData_accumulator)
    con.close()
    return riderRouteData_accumulator


def retrieveDriverDataWithName(name):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE name='{name}'")
    driverDataWithName = cur.fetchall()
    print("driverDataWithName: - ", driverDataWithName)
    con.close()
    return driverDataWithName


def retrieveRiderDataWithName(name):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE name='{name}'")
    riderDataWithName = cur.fetchall()
    print("riderDataWithName: - ", riderDataWithName)
    con.close()
    return riderDataWithName


def retrieveDriverDataWithEmail(email):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE email='{email}'")
    driverDataWithEmail = cur.fetchall()
    con.close()
    return driverDataWithEmail


def retrieveDriverDataWithLicenseNumber(licenseNumber):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE licenseNumber='{licenseNumber}'")
    driverDataWithLicenseNumber = cur.fetchall()
    con.close()
    return driverDataWithLicenseNumber


def retrieveRiderDataWithEmail(email):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE email='{email}'")
    riderDataWithEmail = cur.fetchall()
    con.close()
    return riderDataWithEmail


def retrieveDriverDataWithNameAndPassword(name, password):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE name='{name}' AND password='{password}'")
    driverDataWithNameAndPwd = cur.fetchall()
    con.close()
    return driverDataWithNameAndPwd


def retrieveRiderDataWithNameAndPassword(name, password):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE name='{name}' AND password='{password}'")
    riderDataWithNameAndPwd = cur.fetchall()
    con.close()
    return riderDataWithNameAndPwd


def retrieveDriverDataWithEmailAndPassword(email, password):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE email='{email}' AND password='{password}'")
    driverDataWithEmailAndPwd = cur.fetchall()
    con.close()
    return driverDataWithEmailAndPwd


def retrieveRiderDataWithEmailAndPassword(email, password):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE email='{email}' AND password='{password}'")
    riderDataWithEmailAndPwd = cur.fetchall()
    con.close()
    return riderDataWithEmailAndPwd


def retrieveDriverRouteDataWithName(name):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driverRoute WHERE name='{name}' ORDER BY id DESC LIMIT 1")
    driverRouteDataWithName = cur.fetchall()
    driverRouteData_accumulator = []
    for item in driverRouteDataWithName:
        driverDataDict = {"id": item[0], "name": item[1], "source": item[2], "destination": item[3],
                          "availableSeats": item[4], "starttime": item[5], "endtime": item[6], "rider1": item[7],
                          "rideStatus": item[8], "rider2": item[9]}
        driverRouteData_accumulator.append(driverDataDict)
    print("driverRouteData_accumulator =", driverRouteData_accumulator)
    con.close()
    return driverRouteData_accumulator


def retrieveRiderRouteDataWithNameSourceDestination(name, source, destination):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM riderRoute WHERE name='{name}' AND source='{source}' AND destination='{destination}'")
    riderRouteDataWithName = cur.fetchall()
    riderRouteData_accumulator = []
    for item in riderRouteDataWithName:
        riderDataDict = {"id": item[0], "name": item[1], "source": item[2], "destination": item[3], "time": item[4],
                         "confirmRideStatus": item[5], "driverName": item[6]}
        riderRouteData_accumulator.append(riderDataDict)
    print("riderRouteData_accumulator =", riderRouteData_accumulator)
    con.close()
    return riderRouteData_accumulator


def retrieveDriverRouteDataWithSourceAndDestination(source, destination):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driverRoute WHERE source='{source}' AND destination='{destination}'")
    driverRouteDataWithSrcDes = cur.fetchall()
    driverRouteData_accumulator = []
    for item in driverRouteDataWithSrcDes:
        driverDataDict = {"id": item[0], "name": item[1], "source": item[2], "destination": item[3],
                          "availableSeats": item[4], "starttime": item[5], "endtime": item[6], "rider1": item[7],
                          "rideStatus": item[8], "rider2": item[9]}
        driverRouteData_accumulator.append(driverDataDict)
    print("driverRouteData_accumulator =", driverRouteData_accumulator)
    con.close()
    return driverRouteData_accumulator


def retrieveRiderRouteDataWithSourceAndDestination(source, destination):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM riderRoute WHERE source='{source}' AND destination='{destination}'")
    riderRouteDataWithSrcDes = cur.fetchall()
    riderRouteData_accumulator = []
    for item in riderRouteDataWithSrcDes:
        riderDataDict = {"id": item[0], "name": item[1], "source": item[2], "destination": item[3], "time": item[4], "confirmRideStatus": item[5], "driverName": item[6]}
        riderRouteData_accumulator.append(riderDataDict)
    print("riderRouteData_accumulator =", riderRouteData_accumulator)
    con.close()
    return riderRouteData_accumulator


def retrieveRiderRouteDataWithSourceAndDestination(source, destination):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM riderRoute WHERE source='{source}' AND destination='{destination}'")
    riderRouteDataWithSrcDes = cur.fetchall()
    riderRouteData_accumulator = []
    for item in riderRouteDataWithSrcDes:
        riderDataDict = {"id": item[0], "name": item[1], "source": item[2], "destination": item[3], "time": item[4], "confirmRideStatus": item[5], "driverName": item[6]}
        riderRouteData_accumulator.append(riderDataDict)
    print("riderRouteData_accumulator =", riderRouteData_accumulator)
    con.close()
    return riderRouteData_accumulator


def updateDriverRouteDataWithRiderName(driveName, source, destination, riderName, time):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    # Updating - ,availableSeats=''
    cur.execute(
        f"UPDATE driverRoute SET rider1 = '{riderName}'  WHERE name='{driveName}' AND source='{source}' AND destination='{destination}' AND starttime='{time}';")
    con.commit()
    con.close()


def updateRiderRouteDataWithDriverName(driveName, source, destination, riderName, time):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    # Updating
    cur.execute(
        f"UPDATE riderRoute SET driverName = '{driveName}', confirmRideStatus = '1' WHERE name='{riderName}' AND source='{source}' AND destination='{destination}' AND starttime='{time}';")
    con.commit()
    con.close()


def updateRiderRouteStatus(riderName):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    # Updating
    cur.execute(
        f"UPDATE riderRoute SET confirmRideStatus = '0' WHERE name='{riderName}';")
    con.commit()
    con.close()


def updateDriverRouteRideStatus(driveName, source, destination, time):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    # Updating
    cur.execute(
        f"UPDATE driverRoute SET rideStatus = '1' WHERE name='{driveName}' AND source='{source}' AND destination='{destination}' AND starttime='{time}';")
    con.commit()
    con.close()


def updateDriverBalanceWithName(name, balance):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    # Updating
    cur.execute(
        f"UPDATE driver SET balance = '{balance}'  WHERE name='{name}';")
    con.commit()
    con.close()


def updateRiderBalanceWithName(name, balance):
    con = sql.connect(r"C:\Users\snehal\PycharmProjects\KaarpoolBlockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    # Updating
    cur.execute(
        f"UPDATE rider SET balance = '{balance}' WHERE name='{name}';")
    con.commit()
    con.close()


# createRiderTableIfNotExist()
# createDriverTableIfNotExist()
# createRiderRouteTableIfNotExist()
# createDriverRouteTableIfNotExist()


# insertDriverData(name='driver', contactNo="9999999999", password="12345", gender="Male", email="driver@gmail.com", vehicle="4 wheeler", licenseNumber="lic115621", licenseValidity="20-05-2025", insuranceNumber="ins115621")
#
# insertRiderData(name='rider', contactNo="8888888888", password="12345", gender="Male", email="rider@gmail.com")

# insertDriverRouteData(name, source, destination, availableSeats, starttime, endtime)
#
# insertRiderRouteData(name, source, destination, time)

# print(retrieveRiderData())
# print(retrieveDriverData())


# updateRiderRouteStatus('rider')
#
# print(retrieveRiderRouteData())
# print(retrieveDriverRouteData())
# print(retrieveCorpusData())
# print(retrieveCorpusDataWithItemName("python"))
# retrieveDriverRouteData()
# retrieveDriverRouteDataWithName("raj")
# retrieveDriverData()
# retrieveRiderData()
# retrieveRiderRouteData()
