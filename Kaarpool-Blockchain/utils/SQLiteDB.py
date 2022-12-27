import sqlite3 as sql


def createRiderTableIfNotExist():
    sqlConnection = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS rider (
                            id integer primary key autoincrement,
                            name text not null,
                            contactNo text not null,
                            password text not null,
                            gender text not null,
                            email text not null
                        );
                    """)


def createDriverTableIfNotExist():
    sqlConnection = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
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
                            insuranceNumber integer not null
                        );
                    """)


def createRiderRouteTableIfNotExist():
    sqlConnection = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderRouteData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS riderRoute (
                            id integer primary key autoincrement,
                            name text not null,
                            source text not null,
                            destination text not null,
                            time text not null
                        );
                    """)


def createDriverRouteTableIfNotExist():
    sqlConnection = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverRouteData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS driverRoute (
                            id integer primary key autoincrement,
                            name text not null,
                            source text not null,
                            destination text not null,
                            availableSeats integer not null,
                            starttime text not null,
                            endtime text
                        );
                    """)


# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())

def insertDriverData(name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity, insuranceNumber):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()

    cur.execute(
        "INSERT INTO driver (name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity, insuranceNumber) VALUES (?,?,?,?,?,?,?,?,?)",
        (name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity, insuranceNumber))
    con.commit()
    con.close()


def insertRiderData(name, contactNo, password, gender, email):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO rider (name, contactNo, password, gender, email) VALUES (?,?,?,?,?)",
                (name, contactNo, password, gender, email))
    con.commit()
    con.close()


def insertDriverRouteData(name, source, destination, availableSeats, starttime, endtime):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO driverRoute (name, source, destination, availableSeats, starttime, endtime) VALUES (?,?,?,?,?,?)",
        (name, source, destination, availableSeats, starttime, endtime))
    con.commit()
    con.close()


def insertRiderRouteData(name, source, destination, time):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO riderRoute (name, source, destination, time) VALUES (?,?,?,?)",
                (name, source, destination, time))
    con.commit()
    con.close()


def retrieveDriverData():
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM driver")
    driverData = cur.fetchall()
    con.close()
    return driverData


def retrieveRiderData():
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM rider")
    riderData = cur.fetchall()
    con.close()
    return riderData


def retrieveDriverRouteData():
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM driverRoute")
    driverRouteData = cur.fetchall()
    con.close()
    return driverRouteData


def retrieveRiderRouteData():
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM riderRoute")
    riderRouteData = cur.fetchall()
    con.close()
    return riderRouteData


def retrieveDriverDataWithName(name):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE name='{name}'")
    driverDataWithName = cur.fetchall()
    con.close()
    return driverDataWithName


def retrieveRiderDataWithName(name):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE name='{name}'")
    riderDataWithName = cur.fetchall()
    con.close()
    return riderDataWithName


def retrieveDriverDataWithEmail(email):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE email='{email}'")
    driverDataWithEmail = cur.fetchall()
    con.close()
    return driverDataWithEmail


def retrieveDriverDataWithLicenseNumber(licenseNumber):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE licenseNumber='{licenseNumber}'")
    driverDataWithLicenseNumber = cur.fetchall()
    con.close()
    return driverDataWithLicenseNumber


def retrieveRiderDataWithEmail(email):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE email='{email}'")
    riderDataWithEmail = cur.fetchall()
    con.close()
    return riderDataWithEmail


def retrieveDriverDataWithNameAndPassword(name, password):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE name='{name}' AND password='{password}'")
    driverDataWithNameAndPwd = cur.fetchall()
    con.close()
    return driverDataWithNameAndPwd


def retrieveRiderDataWithNameAndPassword(name, password):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE name='{name}' AND password='{password}'")
    riderDataWithNameAndPwd = cur.fetchall()
    con.close()
    return riderDataWithNameAndPwd


def retrieveDriverDataWithEmailAndPassword(email, password):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE email='{email}' AND password='{password}'")
    driverDataWithEmailAndPwd = cur.fetchall()
    con.close()
    return driverDataWithEmailAndPwd


def retrieveRiderDataWithEmailAndPassword(email, password):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE email='{email}' AND password='{password}'")
    riderDataWithEmailAndPwd = cur.fetchall()
    con.close()
    return riderDataWithEmailAndPwd


def retrieveDriverRouteDataWithName(name):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driverRoute WHERE name='{name}'")
    driverRouteDataWithName = cur.fetchall()
    driverRouteData_accumulator = []
    for item in driverRouteDataWithName:
        driverRouteData_accumulator.append({k: item[k] for k in item.keys()})
    con.close()
    return driverRouteData_accumulator


def retrieveRiderRouteDataWithName(name):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM riderRoute WHERE name='{name}'")
    riderRouteDataWithName = cur.fetchall()
    con.close()
    return riderRouteDataWithName


def retrieveDriverRouteDataWithSourceAndDestination(source, destination):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\driverRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driverRoute WHERE source='{source}' AND destination='{destination}'")
    driverRouteDataWithSrcDes = cur.fetchall()
    con.close()
    return driverRouteDataWithSrcDes


def retrieveRiderRouteDataWithSourceAndDestination(source, destination):
    con = sql.connect(r"E:\blockchain\Kaarpool-Blockchain\utils\SQLiteDB\riderRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM riderRoute WHERE source='{source}' AND destination='{destination}'")
    riderRouteDataWithSrcDes = cur.fetchall()
    riderRouteData_accumulator = []
    for item in riderRouteDataWithSrcDes:
        riderRouteData_accumulator.append({k: item[k] for k in item.keys()})
    con.close()
    return riderRouteData_accumulator


# createRiderTableIfNotExist()
# createDriverTableIfNotExist()
# createRiderRouteTableIfNotExist()
# createDriverRouteTableIfNotExist()

# insertRecipeData("python", pythonData)
# print(retrieveCorpusData())
# print(retrieveCorpusDataWithItemName("python"))
