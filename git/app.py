from flask import Flask, jsonify, request,render_template
from flask_mysqldb import MySQL
from database import  db, app          

class Crud:
    
    cur=db.cursor()
    
    def __init__(self):
        pass
    def get(self):
        resultValue = self.cur.execute("SELECT * FROM store")
        print(resultValue)
        if resultValue > 0:
            userDetails = self.cur.fetchall()
            print(userDetails)
            return jsonify(userDetails=userDetails)  
    

    def post(self,request_data):
        new_store = {
        'name': request_data['name'],
        'price': request_data['price']
        }
        self.cur.execute("INSERT INTO store(name1, price) VALUES(%s, %s)",(request_data['name'], request_data['price']))
        db.commit()
        return jsonify(new_store)
    

    def patch(self,request_data):
        new_store = {
        'name': request_data['name'],
        'price': request_data['price']
        }
        self.cur.execute("UPDATE  store SET price =(%s) WHERE name1= (%s)",(request_data['price'], request_data['name']))
        db.commit()
        return jsonify(new_store)
    
    def put(self, request_data):
        new_store = {
        'name': request_data['name'],
        'price': request_data['price']
        }
        resultValue = self.cur.execute("SELECT * FROM store where name1='name' ")
        if resultValue > 0:
            self.cur.execute("UPDATE  store SET price =(%s) WHERE name1= (%s)",(request_data['price'], request_data['name']))
            db.commit()
            self.cur.close()
            return jsonify(new_store)
        else:
            self.cur.execute("INSERT INTO store(name1, price) VALUES(%s, %s)",(request_data['name'], request_data['price']))
            db.commit()
            return jsonify(new_store)


