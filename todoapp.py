from flask import Flask, render_template, request, redirect, url_for  # librerias
import numpy as np

app = Flask(__name__)  # incializar variable

#arreglos Cliente
Nombre_Cliente = []
Nombre_Telefono = []
Nombre_Estado = []

# funcion de bienvenida
@app.route('/')
def index():
    return render_template('index.html', NombreClienteLista = Nombre_Cliente )       #pasa el parametro al index

#add_tareas
@app.route('/registros', methods=['POST'])  # recive atravez del metodo POST
def enviar():
   if request.method == 'POST':
      # almacena el nombre 
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

      #print(Cliente_Nombre)
      return redirect(url_for('index'))   


#segunda ruta
@app.route('/Sesion')    
def Inicio_Sesion():
   
    return render_template('Sesion.html')


@app.route('/Iniciar ', methods=['POST'])   
def Iniciar():
    if request.method == 'POST':
        InicioNombre = request.form['IniciarSesion']
        lst = np.array(Nombre_Cliente)
        result = np.where(lst == InicioNombre)
        print("result")  
        if(result):
            return render_template('Sesion')
        else:
            return redirect(url_for('index'))   
    
        #return render_template('Sesion')

# main del programa
if __name__ == '__main__':
    app.run(debug=True)


