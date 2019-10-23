import sqlite3  # enable control of an sqlite database

DB_FILE = "wiki.db"
db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops

# check_users()
# - @return boolean value
#   - true if the username and password match an entry in the users table
#   - false if the usernmae and password DO NOT match an entry in the users table
def check_users(username, password):
    query = "SELECT username, password FROM users WHERE users.username = \"%s\" AND users.password = \"%s\";" % (username, password)
    response = list(c.execute(query))
    if len(response) == 1:
        return True
    else:
        return False