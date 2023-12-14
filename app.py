import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px


# Sample Data (Replace this with your actual data)
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Brazil', 'Italy', 'Canada'],
    'Population': [331002651, 1439323776, 125584838, 83783942, 1380004385, 67886011, 65273511, 212559417, 60461826, 37742154],
    'GDP': [21427700, 14342903, 5081776, 3845630, 2875148, 2827129, 2777539, 1976948, 1849477, 1643323],
    'PerCapitaIncome': [65212, 11218, 40285, 45699, 2099, 43173, 42658, 8717, 31952, 45085],
    'AvgSalary': [60000, 12000, 50000, 55000, 1500, 50000, 48000, 8000, 40000, 60000]
}

df = pd.DataFrame(data)

# Sorting by GDP to get top 10 countries by GDP
df = df.nlargest(10, 'GDP')

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# Layout of the app
app.layout = html.Div([
    html.H1("Top 10 Countries: Different Criteria"),
    
    # Dropdown for selecting criteria
    dcc.Dropdown(
        id='criteria-dropdown',
        options=dropdown_options,
        value='Population'  # Default value
    ),
    
    # Bar chart for displaying selected criteria
    dcc.Graph(id='bar-chart')
])

# Callback to update the bar chart based on the selected criteria
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('criteria-dropdown', 'value')]
)
def update_bar_chart(selected_criteria):
    fig = px.bar(df, x='Country', y=selected_criteria, title=f'{selected_criteria} of Top 10 Countries')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
