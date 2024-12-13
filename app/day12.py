from dash import dcc, html, Input, Output, callback
import plotly.graph_objs as go
from src.day12 import *

page_layout = html.Div([
  html.H1("Day 12: Garden Groups"),
  dcc.Textarea(
    id='day12-puzzle-input',
    placeholder='Puzzle Input...',
    style={'width': '100%', 'height': 200},
    value='''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''
  ),
  dcc.Graph(id='day12-garden'),
  html.Div(id='day12-part1', style={'margin': '10px', 'fontSize': '18px', 'color': 'red'}),
  html.Div(id='day12-part2', style={'margin': '10px', 'fontSize': '18px', 'color': 'green'})
])

@callback(
  [Output('day12-garden', 'figure'),
   Output('day12-part1', 'children'),
   Output('day12-part2', 'children')],
  [Input('day12-puzzle-input', 'value')]
)
def update_graph_and_labels(text):
  if not text:
    return go.Figure(), "", ""

  garden = Garden(text)

  part1 = f"Part 1: Total Price = {garden.price}"
  part2 = f"Part 2: Total Price with Bulk Discount = {garden.bulk_price}"

  region_by_id = {}
  region_number = {}
  region_of_node = {}
  for region in garden.regions:
    region_by_id[region.id] = region
    region_number[region.id] = len(region_number)
    for node in region.nodes:
      region_of_node[node] = region.id

  heatmap_data = []
  heatmap_custom_data = []
  for y in range(garden.height):
    heatmap_row = []
    heatmap_custom_row = []
    for x in range(garden.width):
      region_id = region_of_node[complex(x, y)]
      region = region_by_id[region_id]
      heatmap_row.append(region_number[region_id])
      heatmap_custom_row.append([
        region.label, region_id, region.area,
        region.perimeter, region.price,
        region.sides, region.bulk_price
      ])
    heatmap_data.append(heatmap_row)
    heatmap_custom_data.append(heatmap_custom_row)

  figure = go.Figure(data=go.Heatmap(
    z=heatmap_data,
    customdata=heatmap_custom_data,
    colorscale='Rainbow',
    showscale=False,
    hoverinfo='text',
    hovertext=None
  ))

  figure.update_layout(
    xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
    yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, autorange='reversed'),
    width=800,
    height=600,
    margin=dict(l=20, r=20, t=20, b=20)
  )

  figure.update_traces(
    hovertemplate=(
      "<b>Coordinates:</b> (%{x}, %{y})<br>"
      "<b>Type of plant:</b> %{customdata[0]}<br>"
      "<b>Region ID:</b> %{customdata[1]}<br>"
      "<b>Area:</b> %{customdata[2]}<br>"
      "<b>Perimeter:</b> %{customdata[3]}<br>"
      "<b>Fence Price:</b> %{customdata[4]}<br>"
      "<b>Sides:</b> %{customdata[5]}<br>"
      "<b>Fence Bulk Price:</b> %{customdata[6]}<extra></extra>"
    )
  )

  return figure, part1, part2
