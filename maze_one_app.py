from geradordelabirinto import get_labirinto
from maoesquerda import maoEsquerda, classifica





from flask import Flask
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
@app.route('/')
def serve_ari():
    labirinto = get_labirinto()
    caminho = maoEsquerda(labirinto)
    dificuldade = classifica(caminho)
    labirintobj = {
        "labirinto": labirinto.tolist(),
        "caminho" : caminho,
        "dificuldade" : dificuldade,
        "inicio" : caminho[0],
        "fim" : caminho[-1]
   }
    print(type(labirintobj))
    app_json = json.dumps(labirintobj)
    return app_json


print(serve_ari())
