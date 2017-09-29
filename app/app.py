# ---inicio --  inportação da bibliotecas 
from flask import Flask, render_template, request, url_for, redirect

from flask.exit.sqlalchemy import SQLAlchemy
# -- fim ---- importação das bibliotecas ----

# --- inicio configuração do banco de dados ---
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'

db = SQLAlchemy(app)
# --- fim configuração do banco de dados ---
app = Flask(__name__)
# ----inicio do bd Pessoa ------
class Cliente(db.Model):
    __tablename__='cliente'

    __id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    cpf = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    
# ----fim do bd Pessoa ------
# ----inicio -- valores que seram recebidos do formulario html ------

    def __init__(self, nome, telefone, cpf, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.senha = senha

db.create_all()

class Produto(db.Model):
    __tablename__='cliente'

    __id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    produto = db.Column(db.String)
    quant = db.Column(db.Integer)
    descricao = db.Column(db.String)
    foto = db.Column(db.String)
    valor = db.Column(db.Integer)
    
    

    def __init__(self, produto, quant, descricao):
        self.produto = produto
        self.quant = quant
        self.descricao = descricao
        self.foto = foto
        self.valor = db.Column(db.Integer)

db.create_all()

class Categoria (db.Model):
    __tablename__='categoria'

    __id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    categoria = db.Column(db.String)
    
    def __init__(self, categoria):
        self.categoria = categoria
        

db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/Clientes")
def clientes()
    return render_template("cliente.html")
@app.route("/admin")
def admin():
    return render_template("admin/admin.html")
@app.route("/cad_cliente",methods=['GET','POST'])
def cad_cliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        senha = request.form.get("senha")

@app.route("/cad_produtos",methods=['GET','POST'])
def cad_produtos():
    if request.method == "POST":
        produto = request.form.get("produto")
        quant = request.form.get("quant")

@app.route("/cad_categoria",methods=['GET','POST']
def cad_categoria():
           if request.method == "POST":
               categoria = request.form.get("categoria")

