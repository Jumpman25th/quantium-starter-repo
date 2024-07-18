# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
app.layout = dcc.RadioItems(['north', 'west', 'south', 'east', 'all'])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('filtered_data_csv')

# Aggregate data by Date and Region, summing the total_value
aggregated_df = df.groupby(['date', 'region'], as_index=False)['sales'].sum()

fig = px.bar(aggregated_df, x="sales", y="date", color="region", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Sales data visualizer'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])


# Define the callback to update the graph
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    fig = px.bar(filtered_df, x="date", y="sales", color="region", barmode="group",
                 labels={"date": "Date", "sales": "Total Sales", "region": "Region"})

    return fig

if __name__ == '__main__':
    app.run(debug=True)
