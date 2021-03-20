from src.connect_bd.bd import mysql
from flask import request, redirect, flash

class DatabaseModel():
    def lists(self):
        
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW DATABASES") 
        data = cursor.fetchall()
        cursor.close()
        return data

    def create(self, nombrebd):

        cursor = mysql.get_db().cursor()
        cursor.execute("CREATE DATABASE `%s`" %nombrebd,)
        mysql.get_db().commit()
        cursor.close()
    
    def listTables(self, namebd):

        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW TABLES FROM `%s`" %namebd)
        data = cursor.fetchall()
        cursor.close()

        return data