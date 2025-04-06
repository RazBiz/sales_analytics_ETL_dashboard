import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine

# Database connection string (use correct credentials for your setup)
DATABASE_URL = "postgresql://postgres:password@localhost:5432/retaildb"  # Update with your connection details

# Create a connection to the database
engine = create_engine(DATABASE_URL)

# Query the sales data from the database
query = "SELECT * FROM sales"  # Adjust the query to match your table and columns
sales = pd.read_sql(query, engine)

# Initialize the dashboard
app = dash.Dash(__name__)

# Create the plot
fig = px.line(sales, x='date', y='total_price', color='store_name', title='Sales Over Time')

# Layout for the dashboard
app.layout = html.Div([
    html.H1("Retail Sales Dashboard"),
    dcc.Graph(figure=fig)
])

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
