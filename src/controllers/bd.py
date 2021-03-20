from src.models.bd import DatabaseModel
from src import app

databaseModel = DatabaseModel()

class DatabaseController():
    def list(self):        
        data = databaseModel.lists()
        return data

    def create(self, nombrebd):
        databaseModel.create(namedb)

    def search(self, based):
        data = databaseModel.listTables(db)
        return data
