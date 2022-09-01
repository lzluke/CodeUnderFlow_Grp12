import shelve
import uuid


class User:
    def __init__(self, username, pw):
        id = str(uuid.uuid4())
        self.__id = id
        self.__username = str(username)
        self.__pw = str(pw)

    def getUsername(self):
        return self.__username

    def getPw(self):
        return self.__pw

    def getId(self):
        return self.__id


def getShelve(key="User"):
    db = shelve.open("db/database")
    try:
        db_copy = db[key]
    except:
        db_copy = {}

    db.close()
    return db_copy


def saveShelve(db_copy, key="User"):
    db = shelve.open("db/database")
    db[key] = db_copy
    db.close()


# Temp User
db_copy = getShelve()
if len(db_copy.keys()) == 0:
    user = User("viadmin", "Orion123")
    db_copy[user.getId()] = user
    saveShelve(db_copy)
