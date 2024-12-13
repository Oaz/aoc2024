import dash
from dash import dcc, html, Input, Output, callback
import app.day12

pages = {
  "/day12": app.day12.page_layout
}

dash_app = dash.Dash(__name__, suppress_callback_exceptions=True)
dash_app.title = "Advent of Code 2024"
server = dash_app.server

dash_app.layout = html.Div([
  dcc.Location(id='url', refresh=False),
  html.Div(id='page-content')
])

main_page_layout = html.Div([
  html.H1("Advent of Code 2024"),
  html.A("Day 12", href="/day12", style={'fontSize': 24, 'color': 'blue', 'textDecoration': 'underline'})
])


@callback(
  Output('page-content', 'children'),
  [Input('url', 'pathname')]
)
def display_page(pathname):
  return pages.get(pathname, main_page_layout)


if __name__ == '__main__':
  dash_app.run_server(debug=True)
