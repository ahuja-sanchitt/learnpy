import mysql.connector
import datetime
__cnx= None

def sql_connection():
   print("Opening mysql connection")
   global __cnx 
    
    
    
    
   if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='admin',host='127.0.0.1',database='gs')

   return __cnx        