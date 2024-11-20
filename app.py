from flask import Flask, render_template, request, url_for# Importamos flask y la funcion para renderizar html mediante su nombre.
app = Flask(__name__) #Creamos nuestra instancia de una aplicacion flask con el nombre de __main__

@app.route('/') #Establecemos una ruta sencilla, la cual retorna un mensaje
def index():
    return render_template("index.html")

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad_tarros = int(request.form["cantidad_tarros"])
        error = None
        tarro = 9000
        if edad < 18:
            descuento = 0
            if edad <= 0:
                error = "La edad no puede ser negativa"
        elif edad >= 18 and edad <= 30:
            descuento = .15
        elif edad > 30:
            descuento = .25
        
        precio = tarro * cantidad_tarros
        descuento_total = precio * descuento
        precio_total = precio - descuento_total
        print(precio_total, request.method)
        return render_template("ejercicio1.html", nombre=nombre, precio=precio, descuento_total=descuento_total, precio_total=precio_total, method = request.method, error = error)
    else:
        return render_template("ejercicio1.html")
@app.route('/ejercicio2', methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombre = request.form["nombre"]
        password = request.form["password"]
        if nombre == "juan" and password == "admin":
            mensaje = "Bienvenido Administrador Juan"
        elif nombre == "pepe" and password == "user":
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template("ejercicio2.html", mensaje = mensaje, method = request.method)
    else:
        return render_template("ejercicio2.html")



if __name__ == "__main__": #Ejecutamos nuestra app si el script fue ejecutado directamente por su nombre
    app.run(debug=True)