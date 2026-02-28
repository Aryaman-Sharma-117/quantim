from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv("output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

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
        id='example-graph-2'
    ),
    html.Div(children='Select a region:', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(style={'textAlign': 'center'}, children=[
        dcc.RadioItems(
            ['north', 'south', 'east', 'west'],
            'north',
            id='region-radio',
            inline=True,
            labelStyle={
                'color': colors['text'],
                'textAlign': 'center',
                'margin-right': '15px'
            }
        )
    ])
        
    
])

@callback(
    Output('example-graph-2', 'figure'),
    Input('region-radio', 'value')
)
def update_figure(selected_region):
    filtered_df = df[df['Region'] == selected_region]

    fig = px.line(filtered_df, x="Date", y="Sales",
                  title='Pink Morsel Sales Over Time')

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
