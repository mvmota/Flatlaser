import dash
import dash_core_components as dcc
import dash_html_components as html
from models import Produto, Cliente
from Estampa import db, app


# Dash de produtos
app_dash = dash.Dash(
    __name__,
    server=app,
    routes_pathname_prefix="/dash/"
)

def obter_dados_produtos():
    dados = db.session.query(
        Produto.material_produto,
        db.func.count(Produto.id_produto)
    ).group_by(Produto.material_produto).all()
    return dados

app_dash.layout = html.Div([
    html.H1("Dashboard de Produtos"),
    dcc.Graph(
        figure={
            "data": [{
                "x": [d[0] for d in obter_dados_produtos()],
                "y": [d[1] for d in obter_dados_produtos()],
                "type": "bar"
            }],
            "layout": {"title": "Produtos por Material"}
        }
    )
])

