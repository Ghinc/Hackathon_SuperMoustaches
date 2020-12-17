# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 06:53:59 2020

@author: Ghinevra Comiti
"""

import mysql.connector
from datetime import datetime


prix_produits=dict() #ce dictionnaire va stocker l'hiistorique des prix du produit
#ainsi que les dates auxquelles ces prix ont été pratiqués


#fonction de connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="produits"
)  


mycursor = mydb.cursor()


#cette fonction obtient le prix actuel du produit choisi,
#et si il a changé, elle ajoute le changement a historique_prix

def get_prix(id_product):
    
    sql=("SELECT price FROM produits WHERE id_product=(%s)")
    val=(id_product,)
    if not id_product in prix_produits.keys():
        prix_produits[id_product]=[]
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    sortie=[]
    for row in result:
        sortie.append(float(row[0]))
    if sortie[0] not in prix_produits[id_product]:
        prix_produits[id_product].append([sortie[0], datetime.now()])
    return(sortie)



def maj_prix_db(id_product, new_price):
    sql=("UPDATE produits SET price=(%s) WHERE id_product=(%s)")
    val=(new_price, id_product)
    mycursor.execute(sql,val)
    
    mydb.commit()
    
get_prix(2)
print(prix_produits[3])