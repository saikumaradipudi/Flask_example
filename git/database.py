from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect(host="localhost",    
                     user="root",        
                     passwd="S@ikumar.1", 
                     db="flaska")       