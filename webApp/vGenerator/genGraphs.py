import boto3
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from random import randint

def test():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig