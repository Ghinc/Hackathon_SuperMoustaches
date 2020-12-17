# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:57:33 2020

@author: Ghinevra Comiti
"""

import mysql.connector
from flask import Flask, request, jsonify 

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="produits"
)  

mycursor = mydb.cursor()

@app.route("/produits", methods=["GET", "POST"])
def all_produits():
    produits=None
    if request.method=='GET':
        sql=("SELECT * FROM produits.produits")
        mycursor.execute(sql)
        produits = [
            dict(id_product_google=row[0], price=row[1], date_creation=row[2], 
                 date_update=row[3],
                 id_product=row[4], reference=row[5])
            for row in mycursor.fetchall()
        ]
        if produits is not None:
            return jsonify(produits)
    
    if request.method=="POST":
        new_id_product_google = request.form["gtin"]
        new_id = request.form["id"]
        new_price = request.form["price"]
        new_reference = request.form["reference"]
        sql = ("INSERT INTO produit (id_product_google, id, price, reference)"
                " VALUES (%s, %s, %s, %s)")
        mycursor.execute(sql, (new_id_product_google, new_id, new_price))
        mydb.commit()
        return (f"Book with the id: 0 created successfully", 201)
    
    
@app.route("/produit/<int:reference>", methods=["GET", "DELETE"])
def single_product(reference):
    
    produit = None
    if request.method == "GET":
        mycursor.execute("SELECT * FROM produits WHERE reference=%s", (reference,))
        rows = mycursor.fetchall()
        for r in rows:
            produit = r
        if produit is not None:
            return jsonify(produit), 200
        else:
            return "ça va pas", 404

    if request.method=="DELETE":
        mycursor.execute("DELETE * FROM produits WHERE reference=%s", (reference,))

    mydb.commit()
    
    
@app.route("/majprix/<int:reference>", methods=["PUT"])
def majprix(reference):
    if request.method == "PUT":
        sql = """UPDATE produit
                SET price=%s,
                WHERE reference=%s """

        price = request.form["price"]
        updated_product = {
            "reference": reference,
            "price": price,
        }
        
        mycursor.execute(sql, (price, reference))
        mydb.commit()
        return jsonify(updated_product)



def insert_db(id_product_google,price,id_product, reference):
    sql=("INSERT INTO produits.produits (id_product_google, price, id_product, reference)"
    " VALUES (reference,%s,%s, %s)")
    val=(id_product_google, price, id_product, reference)
    mycursor.execute(sql,val)
    
    mydb.commit()
    
    
if __name__ == "__main__":
    app.run(debug=True)
    majprix()
  
