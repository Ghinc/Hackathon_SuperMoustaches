import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin 

app = Flask(__name__)
CORS(app, support_credentials=True)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="produits"
)  

mycursor = mydb.cursor(buffered=True)

@app.route("/produits", methods=["GET"])
@cross_origin(supports_credentials=True)
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
    
    
@app.route("/produit/<reference>", methods=["GET", "DELETE"])
@cross_origin(supports_credentials=True)
def single_product(reference):
    
    produit = None
    if request.method == "GET":
        sql=("SELECT * FROM produits.produits WHERE reference=%s")
        var=(reference,)
        print(reference)
        print(var)
        mycursor.execute(sql,var)
        produit = [
            dict(id_product_google=row[0], price=row[1], date_creation=row[2], 
                 date_update=row[3],
                 id_product=row[4], reference=row[5])
            for row in mycursor.fetchall()
        ]
        if produit is not None:
            return jsonify(produit), 200
        else:
            return "ça va pas", 404

    if request.method=="DELETE":
        mycursor.execute("DELETE * FROM produits WHERE reference=%s", (reference,))

    mydb.commit()
    
    
@app.route("/produit/<reference>/price/<new_price>", methods=["GET"])
@cross_origin(supports_credentials=True)
def majprix(reference,new_price):
    mycursor1 = mydb.cursor(buffered=True)
    print(reference, new_price)
    if request.method == "GET":
        sql1=("SELECT price FROM produits WHERE reference=%s" 
              "AND date_update=(SELECT max(date_update) FROM produits)")
        var=(reference,)
        var_suite=(reference, reference)
        sql_id=("SELECT id_product FROM produits WHERE reference=%s"
                "AND numero=(SELECT max(numero)FROM produits WHERE reference=%s)")
        id_product=mycursor1.execute(sql_id,var_suite)
        sql_id_product_google=("SELECT id_product_google FROM produits WHERE reference=%s"
                              "AND numero=(SELECT max(numero)FROM produits WHERE reference=%s)")
        id_product_google=mycursor1.execute(sql_id_product_google,var_suite) 
        sql_date_base=("SELECT date_creation FROM produits WHERE reference=%s "
                       "AND numero=(SELECT max(numero)FROM produits WHERE reference=%s)")
        date_base=mycursor1.execute(sql_date_base,var_suite)
        res1=mycursor1.execute(sql1,var)
        if res1!=new_price:
            sql = ("INSERT INTO produits (id_product_google, id_product, price, reference, date_creation)"
                   " VALUES (%s, %s, %s, %s, %s)")
            val2=(id_product_google, id_product, new_price, reference, date_base)
            mycursor1.execute(sql,val2)
            mydb.commit()
        
        return " c bn",201
    
    #http://127.0.0.1:9090/majprix/2/17
    
@app.route("/histoprix/<reference>", methods=["GET"])
@cross_origin(supports_credentials=True)
def histoprix(reference):
    produits=None
    if request.method=="GET":
        sql=("SELECT price,date_update FROM produits WHERE reference = %s")
        var=(reference,)
        mycursor.execute(sql,var)
        produits = [
            dict(price=row[0], date_update=row[1])
            for row in mycursor.fetchall()
        ]
        if produits is not None:
            return jsonify(produits)


    
    
if __name__ == "__main__":
    app.run(debug=True, port=9090)
