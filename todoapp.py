from flask import Flask, render_template, request, redirect, url_for  # librerias

app = Flask(__name__)  # incializar variable


# funcion de bienvenida
@app.route('/')
def index():
    return render_template('index.html')       #pasa el parametro al index

#arreglos Cliente
Nombre_Cliente = []
Nombre_Telefono = []
Nombre_Estado = []

#add_tareas
@app.route('/registros', methods=['POST'])  # recive atravez del metodo POST
def enviar():
   if request.method == 'POST':
      # almacena el nombre de la tarea
      Cliente_Nombre = request.form['Nombre_Cliente']
      Cliente_Telefono = request.form['Cliente_Telefono']
      Cliente_Estado = request.form['Cliente_estado']
    
      #si faltan datos no ingresa al array 
      if(Cliente_Nombre == "" or Cliente_Telefono == "" or Cliente_Estado == "" ):
          return redirect(url_for('index'))  

      #Almacener datos en los arreglos
      Nombre_Cliente.append(Cliente_Nombre)
      Nombre_Telefono.append(Cliente_Telefono)
      Nombre_Estado.append(Cliente_Estado)

      return redirect(url_for('index'))   

@app.route('/Sesion')     #segunda ruta
def Inicio_Sesion():
    return render_template('Sesion.html')

@app.route('/InicioSesion')     #segunda ruta
def Iniciar():


    return render_template('Sesion.html')


# main del programa
if __name__ == '__main__':
    app.run(debug=True)


