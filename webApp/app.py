from flask import Flask, render_template, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from webApp.vGenerator import genGraphs
import io

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dynamicGph")
def graph1():
    '''
    test use case of returning a graph in html see index.html
    :return:
    '''

    fig = genGraphs.dynamicGph()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')