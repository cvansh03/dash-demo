import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Sample Data (Replace this with your population data)
# For this example, I'll create a simple dataset
data = {
    'Country': ['USA', 'China', 'India', 'Brazil'],
    'Population': [331002651, 1439323776, 1380004385, 212559417]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# Layout of the app
app.layout = html.Div([
    html.H1("Population Visualization"),
    
    # Dropdown for selecting countries
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Country']],
        value='USA'
    ),
    
    # Bar chart for displaying population
    dcc.Graph(id='population-bar-chart')
])

# Callback to update the bar chart based on the selected country
@app.callback(
    Output('population-bar-chart', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_bar_chart(selected_country):
    filtered_df = df[df['Country'] == selected_country]
    
    fig = px.bar(filtered_df, x='Country', y='Population', title=f'Population of {selected_country}')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
