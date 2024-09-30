import os 

SECRET_KEY= 'projetopi'


#Conexão com o banco de dados
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'estampas'
    )
#caminho para as imagens no computador
UPLOAD_PASTA = os.path.dirname(os.path.abspath(__file__)) + '/uploads'