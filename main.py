from flask import Flask, render_template
import mysql.connector

db = mysql.connector.connect(
    host='172.17.3.7',
    user='productos',
    password='productos',
    database='productos',
    port=3306
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")
def index():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute('select * from productos')
    
    productos = cursor.fetchall()
    #producto = cursor.fetchone()
    cursor.close()
    
    return render_template("index.html", productos=productos)

@app.get("/crear")
def crearProducto():
    return render_template("crear.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

@app.get("/contacto/<int:contactoId>/edit")
def editarContacto(contactoId):
    suma = 2+2
    
    return render_template('contactos/editar.html', 
        contactoId = contactoId, 
        suma = suma
    )

#/edad/27 Tu naciste en el año 19

app.run(debug=True)
