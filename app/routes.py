from flask import Flask, render_template
 
app = Flask(__name__)  
# --- incio pages site --- 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/celular')
def celular():
  return render_template('celular.html')

@app.route('/carro')
def carro():
  return render_template('carro.html')

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html')

@app.route('/contato')
def contato():
  return render_template('contato.html')

@app.route('/detalhe')
def detalhes():
  return render_template('detalhe.html')
# --- fim pages site --- 

#----inicio admin--------

@app.route('/admin/login')
def login():
  return render_template('admin/login.html')

@app.route('/admin/admin')
def admin():
  return render_template('admin/admin.html')

@app.route('/admin/cad_categoria')
def categoria():
  return render_template('admin/cad_categoria.html')


@app.route('/admin/lista_categoria')
def lista_cat():
  return render_template('admin/lista_categoria.html')

@app.route('/admin/lista_produto')
def lista_prod():
  return render_template('admin/lista_produto.html')

  
@app.route('/admin/cad_produto')
def produto():
  return render_template('admin/cad_produto.html')

@app.route('/admin/lista_usuario')
def lista_user():
  return render_template('admin/lista_usuario.html')

@app.route('/admin/relatorio')
def relatorio():
  return render_template('admin/relatorio.html')


#----inicio admin--------



 
if __name__ == '__main__':
  app.run(debug=True)
