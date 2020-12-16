# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:57:33 2020

@author: Ghinevra Comiti
"""

import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="produits"
)  

mycursor = mydb.cursor()



def insert_db(id_product_google,price,id_product):
    sql=("INSERT INTO produits.produits (id_product_google, price, id_product)"
    " VALUES (%s,%s,%s)")
    val=(id_product_google, price, id_product)
    mycursor.execute(sql,val)
    
    mydb.commit()
    
    
insert_db(1,45.6,3)

  