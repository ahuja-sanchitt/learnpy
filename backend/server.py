from flask import Flask, request, jsonify
from mysql.connector import connect, connection
from werkzeug.wrappers import response
import product_dao
import json
import unit_s
import orders
from sql_con import sql_connection

app=Flask(__name__)

connection=sql_connection()

@app.route('/')
def home():
    return "Home page here!"

@app.route('/getproducts', methods=['GET'])
def get_products():
    products=product_dao.GetAllProducts(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/getunits', methods=['GET'])
def getunits():
    response = unit_s.get_units(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response    

@app.route('/insertOrder',methods=['POST'])
def insert_order():
    request_payload=json.loads(request.form['data'])
    order_id=orders.insert_order(connection,request_payload)
    response=jsonify({
        'order_id':order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getallorders',methods=['GET'])
def get_all_orders():
    response=orders.get_all_orders(connection)
    response=jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

    
@app.route('/insertProducts',methods=['POST'])
def insert_products():
    request_payload=json.loads(request.form['data'])
    p_id=product_dao.Add_Product(connection,request_payload)
    response=jsonify( { 'p_id':p_id })
    response.headers.add('Acess-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct',methods=['POST'])
def delete_product():
    return_id=product_dao.Delete_Product(connection,request.form['p_id'])
    response=jsonify({ 'p_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__=="__main__":
    print("Starting Python Flask Server for Grocery Store")
    app.run(port=5000)



