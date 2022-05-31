from flask import Flask, render_template, request, redirect, url_for  # librerias

app = Flask(__name__)  # incializar variable


# funcion de bienvenida
@app.route('/')
def index():
    return render_template('index.html', Tarea_Nombre = tareaNombre, Tarea_Correo = correo, Tarea_Prioridad = prioridad )       #pasa el parametro al index

#arreglos
cliente = []
correo = []
prioridad = []

#add_tareas
@app.route('/cliente', methods=['POST'])  # recive atravez del metodo POST
def enviar():
   if request.method == 'POST':
      # almacena el nombre de la tarea
      Nombre_Tarea = request.form['Nombre_Tarea']
      Correo_Tarea = request.form['Correo']
      prioridad_Tarea = request.form['prioridad']
    
      #si faltan datos no ingresa al array 
      if(Nombre_Tarea == "" or Correo_Tarea == "" or prioridad_Tarea == "" ):
          return redirect(url_for('index'))  

      #Almacener datos en los arreglos
      tareaNombre.append(Nombre_Tarea)
      correo.append(Correo_Tarea)
      prioridad.append(prioridad_Tarea)
      
      return redirect(url_for('index'))   



@app.route('/borrar', methods=['POST']) 
def borrar():
    if request.method == 'POST':
      tareaNombre.clear()
      correo.clear()
      prioridad.clear()
      return redirect(url_for('index'))   

# main del programa
if __name__ == '__main__':
    app.run(debug=True)


