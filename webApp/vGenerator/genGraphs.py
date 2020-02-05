import boto3
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from random import randint
import io

def dynamicGph():
    '''
    This essentially returns in Figure class to
    Flask in app.py to display in realtime
    :return:
    '''
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig

def staticGraph():
    '''
    Example where a function such as this must be rendered prior
    to running the Web App
    :return:
    '''
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    xs = range(10)
    ys = range(10)
    axis.plot(xs, ys)

    # you must first go up a directory
    # to save it in the static folder
    fig.savefig("../static/staticGph.png")

if __name__ == '__main__':
    staticGraph()