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

def get_prix(reference):
    
    sql=("SELECT price FROM produits WHERE reference=(%s)")
    val=(reference,)
    if not reference in prix_produits.keys():
        prix_produits[reference]=[]
    mycursor.execute(sql,val)
    result = mycursor.fetchall()
    sortie=[]
    for row in result:
        sortie.append(float(row[0]))
    if sortie[0] not in prix_produits[reference]:
        prix_produits[reference].append([sortie[0], datetime.now()])
    return(sortie)



def maj_prix_db(reference, new_price):
    sql=("UPDATE produits SET price=(%s) WHERE reference=(%s)")
    val=(new_price, reference)
    mycursor.execute(sql,val)
    
    mydb.commit()
    
get_prix(2)
print(prix_produits[3])
