from flask_sqlalchemy import SQLAlchemy
from flask import Flask

class Database(SQLAlchemy):
    def set_flask_app(self, app):
        self.app = app

    def add_database(self, bind:str, url:str):

        #Si no se ha asignado una base de datos se le asigna la primera bd como principal
        if self.app.config.get("SQLALCHEMY_DATABASE_URI") == None:
            self.app.config["SQLALCHEMY_DATABASE_URI"] = url

        #Se agrega la base de datos como un bind
        if self.app.config.get("SQLALCHEMY_BINDS") == None:
            self.app.config["SQLALCHEMY_BINDS"] = {}

        self.app.config["SQLALCHEMY_BINDS"][bind] = url
    
    def init_SQLAlchemy(self):
        self.__init__(self.app)

db = Database()