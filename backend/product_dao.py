
from sql_con import sql_connection

def GetAllProducts(connection):

 cursor=connection.cursor()

 query="select products.p_id, products.name,products.Unit_id,products.price, unit.unit_name from products inner join unit on products.Unit_id=unit.unit_id"
 cursor.execute(query)


 response= []
 for(p_id, name, Unit_id, price, unit_name) in cursor:  
    
    response.append(
        { "p_id": p_id,
          "P_name": name,
          "unit_id": Unit_id,
          "price": price,
          "unit_name": unit_name
        
        
        }
    )

 
 return response


def Add_Product(connection,product):

    cursor=connection.cursor()

    query="insert into `gs`.`products` (`name`, `Unit_id`, `price`) VALUES (%s, %s,%s);"
    data=(product['name'], product['Unit_id'], product['price'])
    cursor.execute(query,data)
    connection.commit()
    product_id=cursor.lastrowid
    return product_id

def Delete_Product(connection,p_id):
    cursor=connection.cursor()
    query=("delete from `gs`.`products` WHERE `p_id` ="+str(p_id))    
    cursor.execute(query)
    print(p_id)
    connection.commit()
    
    

if __name__=='__main__':
    connection=sql_connection()
   