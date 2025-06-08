from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Configuración de la base de datos (XAMPP)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'accesos'

mysql = MySQL(app)

# Ruta principal
@app.route('/')
def index():
    return render_template('base.html')

# Funciones CRUD para Edificios
@app.route('/edificios')
def edificios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM edificio")
    data = cur.fetchall()
    cur.close()
    return render_template('edificios.html', edificios=data)

@app.route('/add_edificio', methods=['POST'])
def add_edificio():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO edificio (nombre) VALUES (%s)", [nombre])
        mysql.connection.commit()
        return redirect(url_for('edificios'))

@app.route('/edit_edificio/<id>', methods=['POST'])
def edit_edificio(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE edificio SET nombre = %s WHERE id = %s", (nombre, id))
        mysql.connection.commit()
        return redirect(url_for('edificios'))

@app.route('/delete_edificio/<id>')
def delete_edificio(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM edificio WHERE id = %s", [id])
    mysql.connection.commit()
    return redirect(url_for('edificios'))

# Funciones CRUD para Pisos
@app.route('/pisos')
def pisos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT p.*, e.nombre as nombre_edificio FROM piso p JOIN edificio e ON p.id_edificio = e.id")
    pisos_data = cur.fetchall()
    
    cur.execute("SELECT * FROM edificio")
    edificios_data = cur.fetchall()
    cur.close()
    
    return render_template('pisos.html', pisos=pisos_data, edificios=edificios_data)

@app.route('/add_piso', methods=['POST'])
def add_piso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        id_edificio = request.form['id_edificio']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO piso (nombre, id_edificio) VALUES (%s, %s)", (nombre, id_edificio))
        mysql.connection.commit()
        return redirect(url_for('pisos'))

@app.route('/edit_piso/<id>', methods=['POST'])
def edit_piso(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        id_edificio = request.form['id_edificio']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE piso SET nombre = %s, id_edificio = %s WHERE id = %s", (nombre, id_edificio, id))
        mysql.connection.commit()
        return redirect(url_for('pisos'))

@app.route('/delete_piso/<id>')
def delete_piso(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM piso WHERE id = %s", [id])
    mysql.connection.commit()
    return redirect(url_for('pisos'))

@app.route('/areas')
def areas():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT a.*, e.nombre as nombre_edificio, p.nombre as nombre_piso 
        FROM area a 
        JOIN edificio e ON a.id_edificio = e.id 
        JOIN piso p ON a.id_piso = p.id
    """)
    areas_data = cur.fetchall()
    
    cur.execute("SELECT * FROM edificio")
    edificios_data = cur.fetchall()
    
    cur.execute("SELECT * FROM piso")
    pisos_data = cur.fetchall()
    cur.close()
    
    return render_template('areas.html', areas=areas_data, edificios=edificios_data, pisos=pisos_data)

@app.route('/get_pisos/<id_edificio>')
def get_pisos(id_edificio):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM piso WHERE id_edificio = %s", [id_edificio])
    pisos = cur.fetchall()
    cur.close()
    
    pisos_list = []
    for piso in pisos:
        pisos_list.append({'id': piso[0], 'nombre': piso[1]})
    
    return jsonify(pisos_list)

@app.route('/add_area', methods=['POST'])
def add_area():
    if request.method == 'POST':
        nombre = request.form['nombre']
        id_piso = request.form['id_piso']
        id_edificio = request.form['id_edificio']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO area (nombre, id_piso, id_edificio) VALUES (%s, %s, %s)", 
                   (nombre, id_piso, id_edificio))
        mysql.connection.commit()
        return redirect(url_for('areas'))

@app.route('/edit_area/<id>', methods=['POST'])
def edit_area(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        id_piso = request.form['id_piso']
        id_edificio = request.form['id_edificio']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE area SET nombre = %s, id_piso = %s, id_edificio = %s WHERE id = %s", 
                   (nombre, id_piso, id_edificio, id))
        mysql.connection.commit()
        return redirect(url_for('areas'))

@app.route('/delete_area/<id>')
def delete_area(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM area WHERE id = %s", [id])
    mysql.connection.commit()
    return redirect(url_for('areas'))

if __name__ == '__main__':
    app.run(debug=True)