#!/usr/bin/python

import dash
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd 
import sqlite3

#connect to sqlite db and convert to dataframe
conn = sqlite3.connect('geo_twitter.db')
df = pd.read_sql_query("SELECT * FROM stream_results", conn)

def generate_table(dataframe, max_rows=50):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash()

app.layout = html.Div(children=[
    html.H4('HCSC Related Tweets (August 2018)'),
    generate_table(df)
])

#style
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
	app.run_server(debug=True)
