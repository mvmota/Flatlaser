#ARQUIVO DE ROTAS


from flask import  render_template, request, redirect, session, flash, url_for, send_from_directory
#importa as variaveis Produto e Usuario do models
from models import Produto, Usuario, Cliente
#importa as variaveis db(conexão com o banco) e app(chama o flask) de Estampa
from Estampa import db, app
from definicoes import recupera_imagem, deletar_imagem
import time

#rota para a página HTML já feita
@app.route('/')
def listarProdutos():  

#obriga estar logado para acessar a pagina inicial   
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    lista = Produto.query.order_by(Produto.id_produto)

#variavel produtos recebe conteudo da variavel lista
    return render_template('Lista_produtos.html',
                            titulo = 'Produtos Cadastrados', 
                            produtos = lista)




#rota para a página HTML cadastra_produtos
@app.route('/cadastrar')
def cadastrar_produtos():

#obriga estar logado para acessar a pagina cadastrar
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))

    return render_template('cadastra_produtos.html',
                           titulo = 'Cadastro de Produtos')



#Retorna o valor informado na pagina de cadastro para a pagina Lista_produtos
@app.route('/adicionar', methods=['POST', ])
def adicionar_produto():
    nome = request.form['txtNome']
    material = request.form['txtMaterial']
    cor = request.form['txtCor']
    tamanho = request.form['txtTamanho']

#Cadastrar produto através da página
    produto = Produto.query.filter_by(nome_produto=nome).first()

    if produto:
        flash("Produto já está cadastrado!")
        return redirect(url_for('listarProdutos'))
    
    novo_produto = Produto(nome_produto = nome, material_produto = material, cor_produto = cor, 
                           tamanho_produto = tamanho)
    
    db.session.add(novo_produto)

    db.session.commit()

    arquivo = request.files['arquivo']
    pasta_arquivos = app.config['UPLOAD_PASTA']
    nome_arquivo = arquivo.filename
    nome_arquivo = nome_arquivo.split('.')
    extensao = nome_arquivo[len(nome_arquivo)-1]
    momento = time.time()
    nome_completo = f'produto{novo_produto.id_produto}_{momento}.{extensao}'
    arquivo.save(f'{pasta_arquivos}/{nome_completo}')

    return redirect(url_for('listarProdutos'))

#ROTA PARA EDITAR_PRODUTO
@app.route('/editar/<int:id>')
def editar(id):

    if session ['usuario_logado']  == None or 'usuario_logado' not in session:
        return redirect (url_for('login'))
    
    produtoBuscado = Produto.query.filter_by (id_produto = id).first()

    album = recupera_imagem(id)
    
    return render_template('editar_produto.html',
                           titulo = 'Editar Produto',
                           produto = produtoBuscado, album_produto = album)

#Editar Produto
@app.route('/atualizar', methods = ['POST', ])
def atualizar():
    produto = Produto.query.filter_by(id_produto = request.form['txtId']).first()
    produto.nome_produto = request.form['txtNome']
    produto.material_produto = request.form['txtMaterial']
    produto.cor_produto = request.form['txtCor']
    produto.tamanho_produto = request.form['txtTamanho']
    db.session.add(produto)
    db.session.commit()
    arquivo = request.files['arquivo']
    pasta_upload = app.config ['UPLOAD_PASTA']
    nome_arquivo = arquivo.filename
    nome_arquivo = nome_arquivo.split('.')
    extensao = nome_arquivo[len(nome_arquivo)-1]
    momento = time.time()
    nome_completo = f'album{produto.id_produto}_{momento}.{extensao}'
    deletar_imagem(produto.id_produto)
    arquivo.save(f'{pasta_upload}/{nome_completo}')
    return redirect(url_for('listarProdutos'))

#Excluir Produtos
@app.route('/excluir/<int:id>')
def excluir(id):
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect (url_for('login'))
    Produto.query.filter_by(id_produto=id).delete()
    deletar_imagem(id)
    db.session.commit()
    flash("Produto Excluido com sucesso")
    return redirect (url_for('listarProdutos'))







##rota para a página HTML já feita para clientes
@app.route('/clientes')
def listarClientes():  
  
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    lista = Cliente.query.order_by(Cliente.id_cliente)

    return render_template('Lista_clientes.html',
                            titulo = 'Clientes Cadastrados', 
                            clientes = lista)



#####rota para a página HTML cadastra_cliente
@app.route('/cadastrar2')
def cadastrar_clientes():

#obriga estar logado para acessar a pagina cadastrar
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))

    return render_template('cadastra_cliente.html',
                           titulo = 'Cadastro de Clientes')



#Retorna o valor informado na pagina de cadastro para a pagina Lista_clientes##verificar rota##
@app.route('/adicionar2', methods=['POST', ])
def adicionar_cliente():
    nome = request.form['txtNome']
    idade = request.form['txtIdade']
    cpf = request.form['txtCPF']
    endereco = request.form['txtEndereco']
    email = request.form['txtEmail']
    telefone = request.form['txtTelefone']

#Cadastrar cliente através da página
    cliente = Cliente.query.filter_by(nome_cliente=nome).first()

    if cliente:
        flash("Cliente já está cadastrado!")
        return redirect(url_for('listarClientes'))
    
    novo_cliente = Cliente(nome_cliente = nome, idade_cliente = idade, cpf_cliente = cpf, 
                           endereço_cliente = endereco, email_cliente = email, telefone_cliente = telefone)
    
    db.session.add(novo_cliente)

    db.session.commit()

    arquivo = request.files['arquivo']
    pasta_arquivos = app.config['UPLOAD_PASTA']
    nome_arquivo = arquivo.filename
    nome_arquivo = nome_arquivo.split('.')
    extensao = nome_arquivo[len(nome_arquivo)-1]
    momento = time.time()
    nome_completo = f'cliente{novo_cliente.id_cliente}_{momento}.{extensao}'
    arquivo.save(f'{pasta_arquivos}/{nome_completo}')

    return redirect(url_for('listarClientes'))

#ROTA PARA EDITAR_CLIENTE
@app.route('/editar2/<int:id>')
def editar2(id):

    if session ['usuario_logado']  == None or 'usuario_logado' not in session:
        return redirect (url_for('login'))
    
    clienteBuscado = Cliente.query.filter_by (id_cliente = id).first()

    album = recupera_imagem(id)
    
    return render_template('editar_cliente.html',
                           titulo = 'Editar Cliente',
                           produto = clienteBuscado, album_produto = album)

#Editar Cliente
@app.route('/atualizar2', methods = ['POST', ])
def atualizar2():
    cliente = Cliente.query.filter_by(id_cliente = request.form['txtId']).first()
    cliente.nome_cliente = request.form['txtNome']
    cliente.idade_cliente = request.form['txtIdade']
    cliente.cpf_cliente = request.form['txtCPF']
    cliente.endereço_cliente = request.form['txtEndereco']
    cliente.email_cliente = request.form['txtEmail']
    cliente.telefone_cliente = request.form['txtTelefone']
    db.session.add(cliente)
    db.session.commit()
    arquivo = request.files['arquivo']
    pasta_upload = app.config ['UPLOAD_PASTA']
    nome_arquivo = arquivo.filename
    nome_arquivo = nome_arquivo.split('.')
    extensao = nome_arquivo[len(nome_arquivo)-1]
    momento = time.time()
    nome_completo = f'album{cliente.id_cliente}_{momento}.{extensao}'
    deletar_imagem(cliente.id_produto)
    arquivo.save(f'{pasta_upload}/{nome_completo}')
    return redirect(url_for('listarClientes'))

#Excluir Clientes
@app.route('/excluir2/<int:id>')
def excluir2(id):
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect (url_for('login'))
    Cliente.query.filter_by(id_cliente=id).delete()
    deletar_imagem(id)
    db.session.commit()
    flash("Cliente Excluido com sucesso")
    return redirect (url_for('listarClientes'))





#rota para a página HTML login
@app.route('/login')
def login():
    return render_template('login.html')


#Codigo para autenticação do usuário
@app.route ('/autenticar', methods=['POST',])
def autenticar():

    usuario = Usuario.query.filter_by(login_usuario = request.form['txtLogin']).first()

    if usuario:

        if request.form['txtSenha'] == usuario.senha_usuario:

            session['usuario_logado'] = request.form['txtLogin']

            flash(f"Seja bem vindo {usuario.login_usuario}! ")

            return redirect(url_for('listarProdutos'))
        
        else:
            flash("Senha inválida")
            return redirect(url_for('login'))
    else:

        flash("Usuário ou Senha incorretos")

        return redirect(url_for('login'))
    

#Rota para Logoff de usuário    
@app.route ('/sair')
def sair():
    session ['usuario_logado'] = None

    return redirect('login')

@app.route('/uploads/<nome_imagem>')
def imagem(nome_imagem):
    return send_from_directory('uploads', nome_imagem)