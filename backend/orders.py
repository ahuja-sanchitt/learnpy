from datetime import datetime
from sql_con import sql_connection
dates=datetime.now()
def insert_order(connection,orders):
    cursor=connection.cursor()
    order_query = "INSERT INTO `gs`.`order` (`customer_name`, `total`, `datetime`) VALUES (%s,%s,%s);" 
    order_data = (orders['customer_name'], orders['grand_total'], dates)        
    cursor.execute(order_query,order_data)   
    order_id=cursor.lastrowid
    
    order_details_query = "INSERT INTO `gs`.`order_det` (`order_id`, `poduct_id`, `quantity`, `total_price`) VALUES (%s,%s,%s,%s);"

    order_details_data = []
    for order_detail_record in orders['order_details']:
            order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)
   
    connection.commit() 
    return order_id

def get_all_orders(connection):
    cursor=connection.cursor()
    query=("SELECT * FROM gs.order")
    cursor.execute(query)

    response=[]
    for(order_id,customer_name,total,datetime) in cursor:
         response.append({
             'order_id':order_id,
             'customer_name':customer_name,
             'total':total,
             'datetime':datetime

         })
    return response     

if __name__ == '__main__':
   

    connection = sql_connection()
   