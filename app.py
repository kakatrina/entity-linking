import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
app = dash.Dash(__name__)
server = app.server
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df=pd.read_csv(r'C:\Users\yueyu\OneDrive\桌面\virginial pilot\clean_article_in_dict.csv')

indicators=df['sections_simple'].unique()
app.layout =html.Div([
    html.Div([
        html.H1('           Virginial Pilot News Distribution Dashboard'),
        html.H2('Choose to see a section\'s distribution'),
        dcc.Dropdown(
            id='section_dropdown',
            options=[{'label': i, 'value': i} for i in indicators],
            multi=False,
            value = df['sections_simple'].min()),
        dcc.Graph(
            id='value-count-bar'),
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        html.H2('Daily Release volume'),
        dcc.Graph(
            id='volume-bar'),
    ], style={'width': '40%', 'display': 'inline-block'})
    ])
@app.callback(Output('value-count-bar','figure'),Input('section_dropdown','value'))
def update_graph(simple):
    count=df[df['sections_simple']==simple]['section'].value_counts().to_frame().reset_index()
    count.columns=['section','value']
    fig = go.Bar(x=count['section'],
                     y=count['value'])
    layout=go.Layout(xaxis={'title':'section'},yaxis={'title':'value'})
    figure=go.Figure(data=fig,layout=layout)
    return figure
@app.callback(Output('volume-bar','figure'),Input('section_dropdown','value'))
def graph(volume):
    time = df[df['sections_simple'] == volume]['time_date'].value_counts().to_frame().reset_index()
    time.columns=['date','volume']
    fig2 = go.Bar(x=time['date'],
                     y=time['volume'])
    layout2=go.Layout(xaxis={'title':'date'},yaxis={'title':'volume'})
    figure2=go.Figure(data=fig2,layout=layout2)
    return figure2
if __name__ == '__main__':
    app.run_server(debug=True)

