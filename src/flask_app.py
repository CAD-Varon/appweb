from flask import Flask, flash, get_flashed_messages, render_template, request, redirect, url_for, message_flashed, send_from_directory, Response
from db import mysql


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='development'
)

@app.route('/')
def home():
    return render_template('partials/inicio.html')
    
@app.route('/prueba', methods=['GET', 'POST'])
def prueba():
    if request.method == 'POST':
        cedula=request.form['cedula']
        nombre=request.form['nombre']
        apellido=request.form['apellido']
        pais=request.form['pais']
        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO datos VALUES(%s, %s, %s, %s)",(cedula, nombre, apellido, pais))
                cur.connection.commit()
                flash("La informacion de recepción se ha agregado correctamente", "success")
            except:
                flash("Ha ocurrido un error al registrar la informacion de recepción", "error")

            return redirect('/prueba')
    else:
        return render_template('partials/pruebaenvio.html')



HOST = 'localhost'
PORT = 4000
DEBUG = True

if(__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)
# contra1234

