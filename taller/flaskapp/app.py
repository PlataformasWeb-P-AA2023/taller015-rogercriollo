from flask import Flask, render_template
import requests
import json
from .config import usuario, clave

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/departamentos")
def departamentos():
    """
    """
    r = requests.get("http://localhost:8000/departamentos/").json()
    print(r)
    return render_template("list_departamentos.html", datos=r)


@app.route("/edificios")
def edificios():
    """
    """
    r = requests.get("http://localhost:8000/edificios/").json()
    return render_template("list_edificios.html", datos=r
                           )


@app.route("/propietarios")
def propietarios():
    """
    """
    r = requests.get("http://localhost:8000/propietario/").json()
    print(r)
    return render_template("list_propietarios.html", datos=r
                           )
