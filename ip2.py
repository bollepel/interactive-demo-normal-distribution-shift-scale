import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from scipy.stats import norm
import numpy as np

def normal(mean,standard):
    return(norm.pdf(x,loc=mean,scale=standard))
x=np.arange(-5, 5, 0.001)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P('Location: mean μ'),
    dcc.Slider(0.1, 5, 0.1,
               value=3,
               id='mean',
               marks=None,
               updatemode='drag'
    ),
    html.P(r'Scale: standard deviation σ'),
    dcc.Slider(0.1, 1, 0.1,
               value=1,
               id='std',
               marks=None,
               updatemode='drag'
    ),
    dcc.Graph(id="plot"),
])




@app.callback(
    Output("plot", "figure"),
    [Input("mean", "value"),
     Input("std", "value")])

def generate_chart(mean, std):
    fig = make_subplots(rows=1, cols=1, specs=[[{"type": "scatter"}]])

    fig.add_trace(go.Scatter(
        # visible=False,
        line=dict(color="black", width=6),
        name=r" μ = " + str(1)+r" σ=" +str(0.5),
        x= x,
        y=normal(1,0.5)),
        row=1, col=1),


    fig.add_trace(go.Scatter(
        # visible=False,
        line=dict(color="red", width=6),
        name=r" μ = " + str(mean)+r" σ=" +str(std),
        x= x,
        y=normal(mean,std)),
        row=1, col=1)
    return fig

app.run_server(debug=True)
