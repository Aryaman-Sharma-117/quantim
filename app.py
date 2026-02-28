# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv("output.csv")

fig = px.line(df, x="Date", y="Sales", title='Pink Morsel Sales Over Time')

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Soul Foods: Pink Morsel price',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
