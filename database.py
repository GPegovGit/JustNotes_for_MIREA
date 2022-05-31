from main import *
import sqlite3 as sl

db = sl.connect('notebd.db')
c = db.cursor()


# c.execute("DROP TABLE notes")

# c.execute("""CREATE TABLE notes (
#     ID INTEGER NOT NULL,
#     Header TEXT NOT NULL,
#     Note TEXT,
#     Time TEXT
# )""")

# c.execute("""CREATE TABLE users (
#     Username TEXT NOT NULL PRIMARY KEY,
#     Password TEXT NOT NULL,
# )""")


def addN(id2, title, text, time):
	c.execute("INSERT INTO notes VALUES (?,?,?,?)", (id2, title, text, time))


def delN(id2):
	c.execute("DELETE from notes where ID = ?", str(id2))


def delAN():
	c.execute("DELETE from notes")


def addU(username, password):
	c.execute("INSERT OR IGNORE INTO users VALUES (?,?)", (username, password))


def delU():
	c.execute("DELETE from users")


def getAll():
	c.execute("SELECT * from notes")

def getU():
	c.execute("SELECT * from users")


