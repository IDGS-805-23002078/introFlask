from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route("/")
def index():
    titulo = "Flask IDGS805"
    lista = ["Juan", "Pedro", "Mario"]
    return render_template("index.html", titulo=titulo, lista=lista)
 
 
@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")
 
 
@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")
 
 
@app.route("/hola")
def hola():
    return render_template("index.html")
 
 
@app.route("/user/<int:id>/<string:name>")
def user(id, name):
    return "ID: {} Nombre: {}".format(id, name)
 
 
@app.route("/formulario")
def formulario():
    return '''
<form method="POST" action="/resultado">
<label for="name">Nombre:</label>
<input type="text" name="n1" required><br><br>
 
        <label for="apaterno">Apellido Paterno:</label>
<input type="text" name="n2" required><br><br>
 
        <button type="submit">Enviar</button>
</form>
    '''
 
 
@app.route("/operasBas", methods=['GET', 'POST'])
def operas1():
    res = 0
    if request.method == "POST":
        n1 = int(request.form.get("n1"))
        n2 = int(request.form.get("n2"))
        res = n1 + n2
 
    return render_template("operasBas.html", res=res)
 
 
@app.route("/resultado", methods=['POST'])
def resultado():
    n1 = int(request.form.get("n1"))
    n2 = int(request.form.get("n2"))
    res = n1 + n2
    return "La suma de {} + {} = {}".format(n1, n2, res)
 
 
if __name__ == "__main__":
    app.run(debug=True)