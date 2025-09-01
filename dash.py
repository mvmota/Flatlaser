import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
from models import Produto
from Estampa import db
from Estampa import app

app_dash = dash.Dash(__name__, server=app, routes_pathname_prefix="/dash/")

def obter_dados():
    dados = db.session.query(Produto.material_produto, db.func.count(Produto.id_produto)).group_by(Produto.material_produto).all()
    return dados

app_dash.layout = html.Div([
    html.H1("Análise de Produtos"),
    dcc.Graph(
        figure={
            "data": [
                {"x": [d[0] for d in obter_dados()], "y": [d[1] for d in obter_dados()], "type": "bar"}
            ],
            "layout": {"title": "Produtos por Material"}
        }
    )
])