from flask import Flask, render_template
import plotly.graph_objs as go
import plotly
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Dados
    categorias = ['A', 'B', 'C', 'D']
    valores = [10, 25, 15, 30]

    # Criar o gráfico de barras
    data = [go.Bar(x=categorias, y=valores)]

    # Converter o gráfico em JSON
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
