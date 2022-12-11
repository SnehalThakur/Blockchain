import sqlite3 as sql


def createRiderTableIfNotExist():
    sqlConnection = sql.connect(r"SQLiteDB\\riderData.db")
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
    sqlConnection = sql.connect(r"SQLiteDB\\driverData.db")
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
                            licenseValidity integer not null
                        );
                    """)


def createRiderRouteTableIfNotExist():
    sqlConnection = sql.connect(r"SQLiteDB\\riderRouteData.db")
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
    sqlConnection = sql.connect(r"SQLiteDB\\driverRouteData.db")
    print(sqlConnection)

    sqlConnection.execute("""
                        CREATE TABLE IF NOT EXISTS driverRoute (
                            id integer primary key autoincrement,
                            name text not null,
                            source text not null,
                            destination text not null,
                            availableSeats integer not null,
                            starttime text not null,
                            endtime text null
                        );
                    """)


# cursor = sqlConnection.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
# print(cursor.fetchall())

def insertDriverData(name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity):
    con = sql.connect("SQLiteDB\\driverData.db")
    cur = con.cursor()

    cur.execute("INSERT INTO driver (name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity) VALUES (?,?,?,?,?,?,?,?)",
                (name, contactNo, password, gender, email, vehicle, licenseNumber, licenseValidity))
    con.commit()
    con.close()


def insertRiderData(name, contactNo, password, gender, email):
    con = sql.connect("SQLiteDB\\riderData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO rider (name, contactNo, password, gender, email) VALUES (?,?,?,?,?)",
                (name, contactNo, password, gender, email))
    con.commit()
    con.close()


def insertDriverRouteData(name, source, destination, availableSeats, starttime, endtime):
    con = sql.connect("SQLiteDB\\driverRouteData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO driverRoute (name, source, destination, availableSeats, starttime, endtime) VALUES (?,?,?,?,?,?)",
                (name, source, destination, availableSeats, starttime, endtime))
    con.commit()
    con.close()


def insertRiderRouteData(name, source, destination, time):
    con = sql.connect("SQLiteDB\\riderRouteData.db")
    cur = con.cursor()
    cur.execute("INSERT INTO riderRoute (name, source, destination, time) VALUES (?,?,?,?)",
                (name, source, destination, time))
    con.commit()
    con.close()


def retrieveDriverData():
    con = sql.connect("SQLiteDB\\driverData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM driver")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveRiderData():
    con = sql.connect("SQLiteDB\\riderData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM rider")
    recipe = cur.fetchall()
    con.close()
    return recipe



def retrieveDriverRouteData():
    con = sql.connect("SQLiteDB\\driverRouteData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM driverRoute")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveRiderRouteData():
    con = sql.connect("SQLiteDB\\riderRouteData.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM riderRoute")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveDriverDataWithName(name):
    con = sql.connect("SQLiteDB\\driverData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driver WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveRiderDataWithName(name):
    con = sql.connect("SQLiteDB\\riderData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM rider WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveDriverRouteDataWithName(name):
    con = sql.connect("SQLiteDB\\driverRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM driverRoute WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


def retrieveRiderRouteDataWithName(name):
    con = sql.connect("SQLiteDB\\riderRouteData.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM riderRoute WHERE name='{name}'")
    recipe = cur.fetchall()
    con.close()
    return recipe


createRiderTableIfNotExist()
createDriverTableIfNotExist()
createRiderRouteTableIfNotExist()
createDriverRouteTableIfNotExist()

# insertRecipeData("python", pythonData)
# print(retrieveCorpusData())
# print(retrieveCorpusDataWithItemName("python"))
