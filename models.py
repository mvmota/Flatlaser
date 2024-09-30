from Estampa import db

#Criação de classe e eigação com tabela produto no banco de dados
class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome_produto = db.Column(db.String(50), nullable = False)
    material_produto = db.Column(db.String(50), nullable = False)
    cor_produto = db.Column(db.String(20), nullable = False)
    tamanho_produto = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Name %r>' %self.name
    
##Criação de classe e eigação com tabela produto no banco de dados
class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome_cliente = db.Column(db.String(100), nullable = False)
    idade_cliente = db.Column(db.Integer, nullable = False)
    cpf_cliente = db.Column(db.String(11), nullable = False)
    endereço_cliente = db.Column(db.String(200), nullable = False)
    email_cliente = db.Column(db.String(100), nullable = False)
    telefone_cliente = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return '<Name %r>' %self.name
    
#Criação de classe e eigação com tabela produto no banco de dados
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome_usuario = db.Column(db.String(100), nullable = False)
    login_usuario = db.Column(db.String(20), nullable = False)
    senha_usuario = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return '<Name %r>' %self.name