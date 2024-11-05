from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)

# Coneccion de Base de Datos
db_config = {
    'user': ' ',
    'password': ' ',
    'host': 'localhost',
    'database': ' ',
    'port': (3306)
}

@app.route("/", methods=["GET"])
def index():
    color = request.args.get("color")  # Get filter parameters from request
    modelo = request.args.get("modelo")
    marca = request.args.get("marca")
    lim_price = request.args.get("lim_price")
    order_price = request.args.get("order_price")
    fecha = request.args.get("fecha")

    # Build the SQL query with filters
    query = "SELECT No_Serie, Modelo, Marca, Precio, Color, fecha, img FROM AUTO"
    filters = []
    if marca:
        filters.append(f"Marca = '{marca}'")
    if modelo:
        filters.append(f"Modelo = '{modelo}'")
    if color:
        filters.append(f"Color = '{color}'")
    if lim_price:
        filters.append(f"Precio <= {lim_price}")
    if fecha:
        filters.append(f"fecha = '{fecha}'")
    if order_price:
        query += " ORDER " + " BY " + f"Precio {order_price}"
    if filters:
        query += " WHERE " + " AND ".join(filters)
    

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    auto = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', auto=auto)

@app.route("/login/")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)