from database.db_connect import db

class User:
    collection = db["users"]

class File:
    collection = db["files"]
