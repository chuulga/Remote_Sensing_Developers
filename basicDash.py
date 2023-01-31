import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

app = dash.Dash()

app.layout = html.Div([
    html.H1('Iris Dataset'),
    dcc.Dropdown(id='iris-dropdown',
                 options=[{'label': i, 'value': i} for i in iris_df.columns[:4]],
                 value='sepal length (cm)'),
    dcc.Graph(id='iris-graph')
])


@app.callback(
    dash.dependencies.Output('iris-graph', 'figure'),
    [dash.dependencies.Input('iris-dropdown', 'value')])
def update_graph(dropdown_value):
    data = []
    for target in iris_df['target'].unique():
        data.append(go.Scatter(x=iris_df[iris_df['target'] == target][dropdown_value],
                              y=iris_df[iris_df['target'] == target]['target'],
                              mode='markers',
                              name=iris.target_names[target]))
    return {'data': data, 'layout': go.Layout(title=dropdown_value)}


if __name__ == '__main__':
    app.run_server()
