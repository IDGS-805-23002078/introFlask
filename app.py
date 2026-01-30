from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app=Flask(__name__)
app.secret_key='clave secreta'

csrf=CSRFProtect()

@app.route("/")
def index():
    titulo='Flask IDGS805'
    lista=['juan', 'pedro', 'carlos']
    return render_template('index.html',titulo=titulo, lista=lista)


@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    alumnos_class=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_class.validate():
        mat=alumnos_class.matricula.data
        nom=alumnos_class.nombre.data
        apa=alumnos_class.apaterno.data
        ama=alumnos_class.amaterno.data
        email=alumnos_class.correo.data

        mensaje='Bienvendio {}'.format(nom)
        flash(mensaje)

    return render_template("alumnos.html", form=alumnos_class, 
                           mat=mat, nom=nom, apa=apa, ama=ama, email=email)

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/hola")
def hola():
    return '<h1>----Hola Nuevo---</h1>'

@app.route("/user/<int:id>/<string:name>")
def user(id, name):
    return 'ID:{} Nombre:{}'.format(id,name)

@app.route("/formulario")
def formulario():
    return '''
       <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
    </form>

'''

@app.route("/operasBas", methods=['GET','POST'])
def opera1():
    res=0
    if request.method == 'POST':
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res= (n1)+int(n2)

    return render_template("operasBas.html", res=res)

@app.route("/resultado", methods=['GET','POST'])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    res= (n1)+int(n2)
    return "La suma de {} + {} = {}".format(n1,n2, res)

if __name__=='__main__':
    csrf.init_app(app)
    app.run(debug=True)
 