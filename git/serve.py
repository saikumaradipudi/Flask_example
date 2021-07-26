from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from database import  db, app   
from app import Crud


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    l=Crud()
    return l.post(request_data)
    

@app.route('/store',methods=['GET'])
def get_all_store_name():
    l=Crud()
    return l.get()
    
    
@app.route('/store', methods=['PUT'])
def create_Update():
    request_data = request.get_json()
    l=Crud()
    return l.put(request_data)
    

@app.route('/store', methods=['PATCH'])
def change_price():
    request_data = request.get_json()
    l=Crud()
    return l.patch(request_data)
   

app.run(port=5000)

if __name__ == 'main':
    app.run(debug=True)
